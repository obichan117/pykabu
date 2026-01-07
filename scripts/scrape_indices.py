#!/usr/bin/env python3
"""
Scrape all available index codes from nikkei225jp.com

This script is used by CI/CD to keep ALL_KNOWN_INDICES up to date.
It discovers all index codes by finding elements with id pattern #V{code}.

Usage:
    python scripts/scrape_indices.py [--update]

Options:
    --update    Update src/pykabu/sources/nikkei225.py with new indices
"""

import re
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def scrape_available_indices() -> dict[str, str]:
    """Scrape all available index codes from the website."""
    from playwright.sync_api import sync_playwright

    indices = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://nikkei225jp.com", wait_until="domcontentloaded")

        # Wait for content to load
        page.wait_for_timeout(1000)

        # Find all elements with id starting with 'V' followed by digits
        elements = page.query_selector_all("[id^='V']")

        for el in elements:
            el_id = el.get_attribute("id")
            if el_id and re.match(r"^V\d+$", el_id):
                code = el_id[1:]  # Remove 'V' prefix

                # Try to find the name from a nearby element or parent
                # The name is usually in a sibling or parent element
                parent = el.evaluate("el => el.closest('tr, div')")
                if parent:
                    # Look for text that might be the index name
                    name_el = page.query_selector(f"#N{code}")
                    if name_el:
                        name = name_el.text_content() or f"Index {code}"
                    else:
                        name = f"Index {code}"
                else:
                    name = f"Index {code}"

                indices[code] = name.strip()

        browser.close()

    return indices


def get_current_indices() -> dict[str, str]:
    """Get the current ALL_KNOWN_INDICES from source."""
    from pykabu.sources.nikkei225 import ALL_KNOWN_INDICES
    return ALL_KNOWN_INDICES.copy()


def format_indices_dict(indices: dict[str, str]) -> str:
    """Format indices dict as Python code."""
    lines = ["ALL_KNOWN_INDICES = {"]

    # Sort by code
    sorted_codes = sorted(indices.keys(), key=lambda x: int(x))

    for code in sorted_codes:
        name = indices[code]
        lines.append(f'    "{code}": "{name}",')

    lines.append("}")
    return "\n".join(lines)


def update_source_file(indices: dict[str, str]) -> bool:
    """Update the source file with new indices."""
    source_file = Path(__file__).parent.parent / "src/pykabu/sources/nikkei225.py"

    content = source_file.read_text()

    # Find and replace ALL_KNOWN_INDICES
    pattern = r"ALL_KNOWN_INDICES = \{[^}]+\}"
    new_dict = format_indices_dict(indices)

    if re.search(pattern, content):
        new_content = re.sub(pattern, new_dict, content)
        source_file.write_text(new_content)
        return True
    return False


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Scrape available index codes")
    parser.add_argument("--update", action="store_true", help="Update source file")
    parser.add_argument("--check", action="store_true", help="Check for changes (exit 1 if changed)")
    args = parser.parse_args()

    print("Scraping available indices from nikkei225jp.com...")
    scraped = scrape_available_indices()
    print(f"Found {len(scraped)} indices")

    current = get_current_indices()
    print(f"Current known indices: {len(current)}")

    # Find differences
    new_codes = set(scraped.keys()) - set(current.keys())
    removed_codes = set(current.keys()) - set(scraped.keys())

    if new_codes:
        print(f"\nNew indices found: {len(new_codes)}")
        for code in sorted(new_codes):
            print(f"  {code}: {scraped[code]}")

    if removed_codes:
        print(f"\nRemoved indices: {len(removed_codes)}")
        for code in sorted(removed_codes):
            print(f"  {code}: {current[code]}")

    if not new_codes and not removed_codes:
        print("\nNo changes detected.")
        return 0

    if args.check:
        print("\nChanges detected!")
        return 1

    if args.update:
        # Merge: keep current names where available, add new
        merged = {**current, **scraped}
        # Remove codes that no longer exist
        for code in removed_codes:
            del merged[code]

        if update_source_file(merged):
            print("\nUpdated src/pykabu/sources/nikkei225.py")
        else:
            print("\nFailed to update source file")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

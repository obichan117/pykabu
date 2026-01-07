# pykabu

Python library and CLI for Japanese stock market data.

## Requirements

- Python 3.10+

## Installation

### Quick Install (Global)

```bash
# 1. Install pykabu
pip install pykabu

# 2. Install browser for market index feature
playwright install chromium
```

### Recommended: Virtual Environment with uv

[uv](https://docs.astral.sh/uv/) is a fast Python package manager written in Rust.

**Step 1: Install uv** (one-time setup)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Step 2: Create virtual environment and install**

```bash
# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows (PowerShell)

# Install pykabu
uv pip install pykabu

# Install browser for market index feature
playwright install chromium
```

### Alternative: pip + venv

```bash
# Create virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows (PowerShell)

# Install pykabu
pip install pykabu

# Install browser for market index feature
playwright install chromium
```

### Platform Notes

- **macOS**: Works out of the box
- **Windows**: Use PowerShell (not CMD)
- **Linux**: If playwright fails, run: `playwright install-deps chromium`

## Quick Start

### CLI

```bash
kabu sche              # Today's schedule
kabu sche -t           # Tomorrow's schedule
kabu sche -w           # This week's schedule
kabu sche -i 3         # Filter by importance (>= 3 stars)

# Market indices
kabu index             # Default 8 indices
kabu index --all       # All known indices (~25)
kabu index --custom    # Custom configured indices

# Nikkei 225 contribution ranking
kabu rank225           # Show top & bottom contributors
kabu rank225 --top     # Top contributors only
kabu rank225 --bottom  # Bottom contributors only

# Sector ranking
kabu rank_sec          # Show top gainers & losers
kabu rank_sec --top    # Top gainers only
kabu rank_sec --bottom # Top losers only

# Configuration
kabu config show                      # Show current config
kabu config set default_importance 3  # Set default star filter
kabu config index list                # List available indices
kabu config index add 212             # Add NASDAQ
```

### Library

```python
from pykabu.sources import nikkei225

# Schedule data
schedule = nikkei225.get_schedule()
today = nikkei225.get_today_schedule()
tomorrow = nikkei225.get_tomorrow_schedule()
week = nikkei225.get_week_schedule()

# Market indices (requires playwright)
indices = nikkei225.get_indices()
```

## Data Sources

| Source | Data | Method |
|--------|------|--------|
| nikkei225jp.com | Economic calendar | HTTP |
| nikkei225jp.com | Market indices | Playwright |
| nikkei225jp.com | Nikkei 225 contribution ranking | Playwright |
| nikkei225jp.com | Sector ranking | Playwright |

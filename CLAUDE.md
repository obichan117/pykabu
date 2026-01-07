# PyKabu - Claude Instructions

## Project Overview
**pykabu** is a Python library + CLI for Japanese stock market data.

- **Package name**: `pykabu` (pip install pykabu)
- **CLI command**: `kabu`
- **Python import**: `from pykabu.sources import nikkei225`

## Architecture

```
src/pykabu/
├── __init__.py
├── sources/              # Library API (for Python users)
│   ├── __init__.py
│   └── nikkei225.py      # from pykabu.sources import nikkei225
├── cli/                  # CLI layer
│   ├── __init__.py
│   ├── main.py           # Entry point (kabu command)
│   └── commands/
│       ├── __init__.py
│       ├── schedule.py   # kabu sche
│       └── index.py      # kabu index
└── utils/
    ├── __init__.py
    ├── http.py           # HTTP client
    └── output.py         # Terminal output formatting
```

## Usage

### As Library
```python
from pykabu.sources import nikkei225

# Schedule
schedule = nikkei225.get_schedule()
today = nikkei225.get_today_schedule()
tomorrow = nikkei225.get_tomorrow_schedule()
week = nikkei225.get_week_schedule()

# Indices (requires playwright)
indices = nikkei225.get_indices()
```

### As CLI
```bash
kabu sche              # Today's schedule
kabu sche -t           # Tomorrow
kabu sche -w           # This week
kabu sche -i 3         # Importance >= 3 stars
kabu index             # Market indices
```

## Data Sources

| Source | Module | HTTP/JS |
|--------|--------|---------|
| nikkei225jp.com | `nikkei225` | Schedule: HTTP, Index: Playwright |

## Adding a New Data Source

1. Create `src/pykabu/sources/<source>.py`
   - Define dataclasses for data items
   - Implement `get_*()` functions
2. Export in `src/pykabu/sources/__init__.py`
3. Create CLI command in `src/pykabu/cli/commands/<cmd>.py`
4. Register in `src/pykabu/cli/main.py`

## Adding a New Command

1. Add function to appropriate source module
2. Create `src/pykabu/cli/commands/<cmd>.py`
3. Register in `cli/main.py`: `cli.add_command(cmd)`

## Code Style
- Type hints required
- Scrapers return dataclasses
- CLI uses `click` decorators
- Output uses `rich` tables with `--plain` fallback
- Keep library (`sources/`) and CLI (`cli/`) separate

## Development
```bash
pip install -e ".[dev]"
playwright install chromium
ruff check .
mypy src/
pytest
```

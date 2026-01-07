# pykabu

Python library and CLI for Japanese stock market data.

## Installation

```bash
pip install pykabu

# For market indices (requires browser automation)
playwright install chromium
```

## CLI Usage

```bash
kabu sche              # Today's schedule
kabu sche -t           # Tomorrow's schedule
kabu sche -w           # This week's schedule
kabu sche -i 3         # Filter by importance (>= 3 stars)
kabu index             # Market indices

# Configuration
kabu config show                      # Show current config
kabu config set default_importance 3  # Set default star filter
```

## Library Usage

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

- [nikkei225jp.com](https://nikkei225jp.com) - Economic calendar and market indices

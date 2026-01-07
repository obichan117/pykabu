# pykabu

Python library and CLI for Japanese stock market data.

## Installation

```bash
pip install pykabu

# For market indices (requires browser automation)
playwright install chromium
```

## Quick Start

### CLI

```bash
kabu sche              # Today's schedule
kabu sche -t           # Tomorrow's schedule
kabu sche -w           # This week's schedule
kabu sche -i 3         # Filter by importance (>= 3 stars)
kabu index             # Market indices
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

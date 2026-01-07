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
├── config.py             # User configuration (~/.config/pykabu/config.json)
├── sources/              # Library API (for Python users)
│   ├── __init__.py
│   └── nikkei225.py      # from pykabu.sources import nikkei225
├── cli/                  # CLI layer
│   ├── __init__.py
│   ├── main.py           # Entry point (kabu command)
│   └── commands/
│       ├── __init__.py
│       ├── schedule.py   # kabu sche
│       ├── index.py      # kabu index
│       └── config.py     # kabu config
└── utils/
    ├── __init__.py
    ├── http.py           # HTTP client
    └── output.py         # Terminal output formatting

scripts/
└── scrape_indices.py     # CI/CD script for updating index codes

docs/                     # MkDocs documentation
├── index.md
├── cli.md
└── api/
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
kabu index             # Market indices (default 8)
kabu index --all       # All known indices
kabu index --custom    # Custom configured indices
kabu config show       # Show config
kabu config index list # List available indices
kabu config index add 212  # Add custom index
```

## Data Sources

| Source | Module | HTTP/JS |
|--------|--------|---------|
| nikkei225jp.com | `nikkei225` | Schedule: HTTP, Index: Playwright |

## Development Workflow

### Git Branching
- **NEVER commit directly to `main`** - always create a feature branch
- Branch naming convention:
  - `feat/<name>` - new features
  - `fix/<name>` - bug fixes
  - `docs/<name>` - documentation only
  - `refactor/<name>` - code refactoring
- Create a PR for review before merging to main
- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`

### Testing Requirements
Before creating a PR, ensure:
1. `pytest` - all tests pass
2. `ruff check .` - no linting errors
3. `mypy src/` - no type errors
4. Add tests for new features/bug fixes

### Documentation Maintenance
Keep these files updated as you develop:
- **`tasks.md`** - Update task status (in progress/completed)
- **`docs/`** - Update when adding/changing CLI commands
- **`README.md`** - Update for user-facing changes
- **`CLAUDE.md`** - Update architecture diagram if structure changes

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

### Setup
```bash
pip install -e ".[dev]"
playwright install chromium
```

### Before Committing
```bash
ruff check .           # Lint
mypy src/              # Type check
pytest                 # Run tests
```

### Full Feature Workflow
1. Create branch: `git checkout -b feat/my-feature`
2. Make changes
3. Update `tasks.md` (mark task in progress)
4. Run tests: `pytest && ruff check . && mypy src/`
5. Update docs if needed (`README.md`, `docs/`)
6. Commit: `git commit -m "feat: add my feature"`
7. Push: `git push -u origin feat/my-feature`
8. Create PR on GitHub
9. After merge, update `tasks.md` (mark completed)

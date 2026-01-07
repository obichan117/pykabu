# PyKabu - Task Tracker

## Completed ✅

### Initial Development
- [x] Project setup with pyproject.toml
- [x] CLI framework with click
- [x] `kabu sche` command (economic schedule)
- [x] Schedule options: `-t` (tomorrow), `-w` (week), `-i` (importance filter)
- [x] `kabu index` command (market indices)
- [x] Rich table output with `--plain` option
- [x] nikkei225jp.com schedule scraper (httpx + HTMLParser)
- [x] nikkei225jp.com index scraper (playwright)

### Project Structure
- [x] Rename project to `pykabu`
- [x] Restructure to `pykabu.sources.*` pattern
- [x] Create CLAUDE.md
- [x] Create tasks.md
- [x] Library/CLI separation

---

## In Progress 🔄

*Nothing currently in progress*

---

## To Do 📋

### Dev Pipeline (High Priority)
- [x] Delete old `src/nikkei225/` directory
- [x] Create .gitignore
- [x] Basic tests for schedule scraper
- [x] GitHub Actions CI workflow
- [x] GitHub Actions publish workflow
- [x] Initialize git repo
- [x] Create GitHub repo
- [x] Set up PyPI trusted publishing *(configure at pypi.org/manage/account/publishing/)*

### More Features
- [ ] Add more data sources
- [ ] Add more CLI commands
- [ ] User config file support

### Documentation
- [x] Update README.md with usage examples
- [x] API documentation (mkdocs)

---

## Ideas / Backlog 💡
- Cache index data locally
- `kabu news` command
- `kabu earnings` command
- Yahoo Finance data source
- JPX data source
- Shell completion support

# CLI Reference

## kabu sche

Display economic schedule from nikkei225jp.com.

```bash
kabu sche [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `-t`, `--tomorrow` | Show tomorrow's schedule |
| `-w`, `--week` | Show this week's schedule |
| `-i`, `--importance INT` | Filter by minimum importance (1-5 stars) |
| `--plain` | Output plain text (no rich formatting) |

### Examples

```bash
# Today's schedule
kabu sche

# Tomorrow's schedule
kabu sche -t

# This week's schedule
kabu sche -w

# Only important events (3+ stars)
kabu sche -i 3

# Plain text output (for scripting)
kabu sche --plain
```

## kabu index

Display market indices from nikkei225jp.com.

!!! note
    This command requires Playwright. Install with: `playwright install chromium`

```bash
kabu index [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `--plain` | Output plain text (no rich formatting) |

### Examples

```bash
# Show market indices
kabu index

# Plain text output
kabu index --plain
```

## kabu config

Manage pykabu configuration. Settings are stored in `~/.config/pykabu/config.json`.

### Subcommands

| Command | Description |
|---------|-------------|
| `show` | Show current configuration |
| `set KEY VALUE` | Set a configuration value |
| `get KEY` | Get a configuration value |
| `path` | Show config file path |

### Available Settings

| Key | Default | Description |
|-----|---------|-------------|
| `default_importance` | `0` | Default star filter for schedule commands (0 = no filter) |

### Examples

```bash
# Show current configuration
kabu config show

# Set default importance filter to 3 stars
kabu config set default_importance 3

# Get a specific value
kabu config get default_importance

# Show config file location
kabu config path
```

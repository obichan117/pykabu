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
| `--all` | Fetch all known indices (~25) |
| `--custom` | Fetch only custom configured indices |
| `--merged` | Fetch default + custom indices |
| `--plain` | Output plain text (no rich formatting) |

### Examples

```bash
# Show default 8 indices
kabu index

# Show all known indices
kabu index --all

# Show only custom configured indices
kabu index --custom

# Show default + custom
kabu index --merged

# Plain text output
kabu index --plain
```

## kabu rank225

Display Nikkei 225 contribution ranking (寄与度ランキング) from nikkei225jp.com.

!!! note
    This command requires Playwright. Install with: `playwright install chromium`

```bash
kabu rank225 [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `--top` | Show only top contributors (寄与度上位) |
| `--bottom` | Show only bottom contributors (寄与度下位) |
| `--plain` | Output plain text (no rich formatting) |

### Examples

```bash
# Show both top and bottom contributors
kabu rank225

# Show only top contributors
kabu rank225 --top

# Show only bottom contributors
kabu rank225 --bottom

# Plain text output
kabu rank225 --plain
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
| `index list` | List all available index codes |
| `index add CODE` | Add a custom index |
| `index remove CODE` | Remove a custom index |
| `index show` | Show custom indices |
| `index clear` | Clear all custom indices |

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

# List all available index codes
kabu config index list

# Add custom indices
kabu config index add 212        # Add NASDAQ
kabu config index add 1001       # Add Bitcoin
kabu config index add 999 --name "My Custom Index"

# Show custom indices
kabu config index show

# Remove a custom index
kabu config index remove 212
```

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

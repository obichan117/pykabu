"""User configuration management for pykabu"""

import json
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".config" / "pykabu"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
    "default_importance": 0,
}


def _ensure_config_dir() -> None:
    """Create config directory if it doesn't exist."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> dict[str, Any]:
    """Load user configuration from file."""
    if not CONFIG_FILE.exists():
        return DEFAULT_CONFIG.copy()

    try:
        with open(CONFIG_FILE) as f:
            config = json.load(f)
        return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, OSError):
        return DEFAULT_CONFIG.copy()


def save_config(config: dict[str, Any]) -> None:
    """Save user configuration to file."""
    _ensure_config_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def get(key: str, default: Any = None) -> Any:
    """Get a configuration value."""
    config = load_config()
    return config.get(key, default)


def set(key: str, value: Any) -> None:
    """Set a configuration value."""
    config = load_config()
    config[key] = value
    save_config(config)


def get_config_path() -> Path:
    """Return the config file path."""
    return CONFIG_FILE

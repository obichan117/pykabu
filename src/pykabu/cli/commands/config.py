"""Config command for kabu CLI"""

import click

from pykabu import config


@click.group()
def cfg():
    """Manage pykabu configuration"""
    pass


@cfg.command("show")
def show():
    """Show current configuration"""
    current = config.load_config()
    click.echo(f"Config file: {config.get_config_path()}")
    click.echo()
    for key, value in current.items():
        click.echo(f"  {key}: {value}")


@cfg.command("set")
@click.argument("key")
@click.argument("value")
def set_value(key: str, value: str):
    """Set a configuration value

    Example: kabu config set default_importance 3
    """
    # Convert value to appropriate type
    if value.isdigit():
        typed_value: str | int = int(value)
    else:
        typed_value = value

    config.set(key, typed_value)
    click.echo(f"Set {key} = {typed_value}")


@cfg.command("get")
@click.argument("key")
def get_value(key: str):
    """Get a configuration value"""
    value = config.get(key)
    if value is None:
        click.echo(f"Key '{key}' not found")
    else:
        click.echo(value)


@cfg.command("path")
def path():
    """Show config file path"""
    click.echo(config.get_config_path())

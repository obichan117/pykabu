"""Main CLI entry point for kabu"""

import click

from pykabu.cli.commands.schedule import sche
from pykabu.cli.commands.index import index


@click.group()
@click.version_option()
def cli():
    """CLI tools for Japanese stock market data"""
    pass


cli.add_command(sche)
cli.add_command(index)


if __name__ == "__main__":
    cli()

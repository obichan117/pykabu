"""Index command for kabu CLI"""

import click

from pykabu.sources import nikkei225
from pykabu.utils.output import TableData, print_table


@click.command()
@click.option("--plain", is_flag=True, help="Output plain text instead of rich table")
def index(plain: bool):
    """Show market indices from nikkei225jp.com"""
    items = nikkei225.get_indices()

    if not items:
        click.echo("No data found.")
        return

    data = TableData(
        title="Market Indices",
        columns=["Name", "Value", "Change", "%"],
        rows=[[item.name, item.value, item.change, item.percent] for item in items],
    )

    print_table(data, plain=plain)

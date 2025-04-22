import click
from bruno.commands.new_entry import new
from bruno.commands.search_entries import search_entries
from bruno.commands.clear_log import clear_all

@click.group()
def cli():
    pass

cli.add_command(new)
cli.add_command(search_entries)
cli.add_command(clear_all)

if __name__ == '__main__':
    cli()
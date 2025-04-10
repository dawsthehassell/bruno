import click
from bruno.commands.view_entries import view_entries
from bruno.commands.new_entry import new
from bruno.commands.search_entries import search_entries

@click.group()
def cli():
    pass

cli.add_command(view_entries)
cli.add_command(new)
cli.add_command(search_entries)

if __name__ == '__main__':
    cli()
import click
from bruno.commands.new_entry import new
from bruno.commands.search_entries import search_entries
from bruno.commands.clear_log import clear_all
from bruno.commands.delete_entry import delete
from bruno.commands.edit_entry import edit_entry
from bruno.commands.export import export

@click.group()
def cli():
    pass

cli.add_command(new)
cli.add_command(search_entries)
cli.add_command(clear_all)
cli.add_command(delete)
cli.add_command(edit_entry)
cli.add_command(export)

if __name__ == '__main__':
    cli()
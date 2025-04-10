import click
from bruno.commands.view_entries import view_entries
from bruno.commands.new_entry import new

@click.group()
def cli():
    pass

cli.add_command(view_entries)
cli.add_command(new)

if __name__ == '__main__':
    cli()
import click
from bruno.commands import new_entry, list_entries

@click.group()
def cli():
    pass

cli.add_command(new_entry.new)
cli.add_command(list_entries.list)

if __name__ == '__main__':
    cli()
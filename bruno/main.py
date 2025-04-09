import click
from bruno.commands.view_entries import view_entries

@click.group()
def cli():
    pass

cli.add_command(view_entries)

if __name__ == '__main__':
    cli()
import click

@click.command(name="new")
def new():
    click.echo("Starting a new entry log...")
    # need to add all the data parameters like date visited, type of experience, etc.
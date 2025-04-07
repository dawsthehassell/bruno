import click

@click.command()
def cli():
    click.echo("Hello Bruno")

if __name__ == '__main__':
    cli()
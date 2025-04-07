import click

@click.command()
def hello():
    click.echo("Hello Bruno")

if __name__ == '__main__':
    hello()
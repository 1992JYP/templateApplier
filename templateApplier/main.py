import click
from . import controller

@click.command()
@click.option('--hash',
                type=click.Choice(['AA','CC']),  prompt=True)


def cli(hash):
    click.echo(f"hello {hash}")


    
if __name__ =="__main__":
    cli()
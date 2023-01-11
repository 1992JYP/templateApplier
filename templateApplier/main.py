import click
from .fileController import controller

@click.command()
@click.option('--hash',
                type=click.Choice(['SP','TB']),  prompt=True)


def cli(hash):
    click.echo(controller.call(hash))


    
if __name__ =="__main__":
    cli()
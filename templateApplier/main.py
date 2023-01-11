import click
from fileController.function import fileRead
from fileController.function import fileChange

@click.command()
@click.option('--hash',
                type=click.Choice(['SP','TB']),  prompt=True)


def cli(hash):
    click.echo(fileChange.change(hash))


    
if __name__ =="__main__":
    cli()
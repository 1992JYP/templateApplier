import click
from templateApplier.fileController.function.sql.sqlCreator import sqlCreator 
from templateApplier.fileController.function.cs.csCreator import csCreator 

from templateApplier.fileController.function.sql.sqlSelector import main as selector

tpDict = {
    'SQL':"sqlCreator()",
    'CS' :"csCreator()"
}

@click.group()
def main():
    pass

@main.command("start")
@click.option('--menu',
                type=click.Choice(['SQL','CS'], case_sensitive=False),
                prompt=True)
def start(menu:str):
    menu = menu.upper()
    creator = eval(tpDict[menu])
    click.echo(creator.readTemplate())

@main.command("sql")
# @click.argument
def sql():
    sqlcreator = sqlCreator()
    click.echo(sqlcreator.change())

main.add_command(selector,'start')
    
if __name__ =="__main__":
    main()
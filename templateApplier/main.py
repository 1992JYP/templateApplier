import sys
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


### 있는거나 잘 만들고 주말에 하자
# @main.command("setting")
# @click.option('--init',is_flag=True)
# def setting(init):
#     """if you want default settings, add option --init"""
#     if init:
#         pass
#     pass

@main.command("sql")
def sql():
    """ 저장 프로시저 생성 템플릿 채우기 """
    sqlcreator = sqlCreator()
    click.echo(sqlcreator.change())
    click.echo(sys.platform)



@main.command("start")
@click.option('--menu',
                type=click.Choice(['SQL','CS'], case_sensitive=False),
                prompt="""
    HELLO, I'm JYP.  
    I maked template applier        default
    plz choose your option""", default = 'SQL')
def start(menu:str):
    """ 시작 옵션 """
    menu = menu.upper()
    creator = eval(tpDict[menu])
    click.echo(creator.readTemplate())

### start 하고 바로 위에 작성한 템플릿 작성 함수로 넘어가는 함수입니다.
### 일반적으로 권장하지 않는다고 합니다. 
### 왜인지는 잘 모르겠습니다. 권장하지 않는 이유도 적어줬으면 참 좋았을텐데 말이죠.
### https://click.palletsprojects.com/en/8.1.x/advanced/#invoking-other-commands
#
# @main.command("start")
# @click.option('--menu',
# @click.pass_context
# def start(ctx,menu:str):
#     menu = menu.upper()
#     creator = eval(tpDict[menu])
#     click.echo(creator.readTemplate())
#     ctx.invoke(sql)

# main.add_command(selector,'start')
    




if __name__ =="__main__":
    main()
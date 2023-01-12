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
@click.help_option('')
def main():
    """
    템플릿 자동 생성기 입니다.\n
    SQL SERVER(MSSQL)의 기본 관리도구인 SSMS(SQL SERVER Management Studio)의
    템플릿 완성 기능을 다른 개발도구(ex: Azure Data Studio) 에서도 쓰고싶어서 만들었습니다.
    파일컨트롤이 꽤 편리해서 아마 CS, HTML, js, json 등의 파일들도 커맨드라인으로 제작이 가능할 것 같습니다.

    다만 라이브러리인 Click에서 커맨드라인 명령어 연속 실행을 별로 안좋아 하는 것 같아서 이부분은 어떻게 처리해야 할지 고민입니다.                  

    현재 완성된 기능은 프로시저 생성 파일이 전부이며 다른 기능을 원하시면 직접 만드시던가, 아니면 제가 다른 기능을 추가할 때까지 기다리시던가,
    
    급하시다면
    박주윤
    신한 110 339 707136 으로 코드 한줄당 1$ 받겠습니다. 전 양심있어서 라인 개수로 세지는 않습니다.
     
    """
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
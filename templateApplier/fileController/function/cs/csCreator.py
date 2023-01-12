import click

class csCreator:
    

    def __init__(self, filename = "PDtemplate.sql") -> None:
        self.templateDict={}
        self.path = "C:/Users/202212002/Documents/공부/templateApplier/"
        self.fileName = filename
        
    def readTemplate(self) -> str:
        sqlText = '신한 110 339 707136 Donate plz'
        
        return sqlText
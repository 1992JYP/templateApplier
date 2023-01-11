def findPattern(sqlLine):

    Return_Dict = {}

    pattern_Stack = []
    stack_Flag = 0
    stack_Start = 0
    stack_End = 0

    forloop_Count = 0

    for i in sqlLine:
        if stack_Flag:
            if i in [">",","]:
                pattern_Stack.append(i)
                
        else:
            if i=="<":
                pattern_Stack.append(i)
                stack_Flag = 1
                stack_Start=forloop_Count

        if len(pattern_Stack)==4:
            stack_End = forloop_Count
            if pattern_Stack==["<",",",",",">"]:
                patter_String = sqlLine[stack_Start:stack_End+1]
                DB_Name,Schema,OBJ_Name = patter_String[1:-1].split(',')
                Return_Dict[DB_Name] = patter_String

            stack_Start=forloop_Count
            stack_End = forloop_Count

            pattern_Stack = []
            stack_Flag=0
            

        forloop_Count +=1

    return Return_Dict


# def replaceFromInput(promptText):
#     a=int(input(promptText))



testString = """

/**  <Ctrl + Shift + M> 을 사용하세요 **/
/** 쿼리 -> 템플릿매개변수값지정 매뉴를 사용하세요 **/

USE [<UseDatabase,,COMM>]
GO

IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = OBJECT_ID(N'[<Procedure_Owner,,dbo>].[<Procedure_Name,sysname,ProcedureName>]') AND OBJECTPROPERTY(ID, N'ISPROCEDURE') = 1)
DROP PROCEDURE <Procedure_Owner,,dbo>.[<Procedure_Name,sysname,ProcedureName>]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/******************************************************************************************
파일명 : <Procedure_Owner,,dbo>.<Procedure_Name,sysname,ProcedureName>.StoredProcedure.sql

<Create_Date,,> <Author,,Name> : <Description,,>

******************************************************************************************/
--<UseDatabase,,COMM>.<Procedure_Owner,,dbo>.<Procedure_Name,sysname,ProcedureName>
CREATE    PROC [<Procedure_Owner,,dbo>].[<Procedure_Name,sysname,ProcedureName>]
				 @CURR_DATE		DATE
				
AS
   
    SET NOCOUNT ON

	SELECT 'EDIT'
	
	
	
GO


"""

testStringList = testString.split('\n')

templateDictFinal = {}
for i in testStringList:
    if findPattern(i):
        templateDictFinal.update(findPattern(i))
#         print(findPattern(i))

# print(len(templateDictFinal))
# print(templateDictFinal)

for i in templateDictFinal.keys():
    replaceName = input(i + " : ")
    testString = testString.replace(templateDictFinal[i],replaceName)
print(testString)
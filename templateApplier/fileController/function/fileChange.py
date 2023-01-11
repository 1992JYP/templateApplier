from . import fileRead

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


def change(hash):

    testString = fileRead.call(hash)

    testStringList = testString.split('\n')

    templateDictFinal = {}
    for i in testStringList:
        if findPattern(i):
            templateDictFinal.update(findPattern(i))

    for i in templateDictFinal.keys():
        replaceName = input(i + " : ")
        testString = testString.replace(templateDictFinal[i],replaceName)
        templateDictFinal[i]=replaceName
    print(testString)

    fileName = f'{templateDictFinal["Procedure_Owner"]}.{templateDictFinal["Procedure_Name"]}.StoredProcedure.sql'

    newFile = open(fileName,'w',encoding='utf-16')

    newFile.write(testString)

    return fileName
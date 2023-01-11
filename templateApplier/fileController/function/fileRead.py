# w = open('C:/Users/202212002/Documents/공부/templateApplier/templateApplier/fileController/test.txt','r')

# text = w.read()
# text = text.replace('a','z')

# w2 = open('test2.txt','w')
# w2.write(text)
# print(text)

def call(hash):
    templatePath = ''
    if hash =="SP":
        templatePath="C:/Users/202212002/Documents/공부/templateApplier/PDtemplate.sql"
    else:
        templatePath="C:/Users/202212002/Documents/공부/templateApplier/PDtemplate.sql"
    
    template=open(templatePath,'r',encoding='utf-16')
    sqlText = template.read()

    template.close()
    return sqlText

if __name__ =="__main__":
    call()


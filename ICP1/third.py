x=input("Enter string:")
num=0
word=0
for i in x:
    if(i.isnumeric()):
        num+=1
    elif(i.isalpha()):
        word+=1


print(num,word)
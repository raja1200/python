str = input("Enter a Sentence : ")

#string to list
strLst = str.split()

#revering the list
revLst = strLst[::-1]
revStr = ""

#list to string 
for i in revLst:
    revStr += i+" "  #space - to separate words
    
print("Reversed String : ",revStr)

    

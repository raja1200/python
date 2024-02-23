fileobject = open("file1.txt")
content = fileobject.read()
lst = content.split()     #default separator is space
longest = lst[0]          #assuming first element is the longest element
for i in lst :
    if len(i) > len(longest):
        longest = i
print("The longest word in the is :",longest)

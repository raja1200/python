fileobject = open("file1.txt")
content = fileobject.read()   #it reads the entire file 
words = content.split()       
print("The Number of Words in the File is ",len(words))
#open
fileobject1 = open("file1.txt", 'r')
fileobject2 = open("file2.txt" , 'w')

#loop to iterate file in line by line using file object
for line in fileobject1 : 
    fileobject2.write(line)

 #To close the written file2 
fileobject2.close()      
print("File Copied Sucessfully !")

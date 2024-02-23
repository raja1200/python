with open("file1.txt") as file1,open("file2.txt",'w') as file2 :
 for letter in file1 :
    file2.write(letter)
print("file copied successfully")

# Files are automatically closed when the 'with' block exits

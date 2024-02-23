row = int(input("Enter Rows :"))          #pyramid pattern
c = 1
for i in range(1,row+1):                #row loop
    for j in range (1,(row-i)+1):       #space loop
        print(" ", end=" ")
    for k in range (0 , i):             #number loop
        print("*"," ",end=" ")
    print("\n")
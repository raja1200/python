n = int(input("Enter a Number :"))
for i in range(2,n):
    if n%i ==0 :
        print("The Number is not prime")
        break                       #this break statement terminates for loop 
    
else:
    print("The given Number is Prime")

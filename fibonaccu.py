row = int(input("Enter rows :"))
first = 0
second = 1
sum = 0
for i in range(1,row+1):
    print(sum)
    first = second
    second = sum
    sum = first + second 


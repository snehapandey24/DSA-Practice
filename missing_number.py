n = int(input("enter total number"))
arr=[]
sum = 0

for i in range(n-1):
    x=int(input("Enter the elements"))
    arr.append(x)

for i in range(n-1):
    sum = sum + arr[i]

total =  (n *(n+1)) //2

missing = total - sum

print("the missing number is", missing)



n = int(input("Enter the size of the array"))
arr =[]
new =[]

for i in range(n):
    x = int(input("enter the elements"))
    arr.append(x)

for i in range(n):  
    if arr[i] not in new:
        new.append(arr[i])

print("Array after removing Duplicates : " ,new)        
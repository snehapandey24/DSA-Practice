n= int(input("enter the size of an array"))
arr = []

for i in range(n):
    x = int(input("Enter the elements"))
    arr.append(x)

for i  in range (n):
    count = 0

for j in range (n):
    if arr[i] == arr[j]:
        count = +1

if arr[i] not in arr[:i]:
    print(arr[i], "→", count, "times")


   
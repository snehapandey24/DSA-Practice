n = int(input("Enter the size of the array"))
arr = []

for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)
is_sorted = True

for i in range(n-1):
    if arr[i+1] < arr[i]:
        is_sorted = False
        break

print(is_sorted) 

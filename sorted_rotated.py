n = int(input("Enter the size of the array"))
arr = []
count = 0
is_sorted = True

for i in range(n):
    x = int(input("Enter the elements:"))
    arr.append(x)

for i in range(n-1) :
   if  arr[i]   > arr[i+1]:
       count+=1

if arr[n-1] > arr[0]:
    count +=1

if count <= 1:
    print("Sorted and Rotated")
else:
    print("Not Sorted and Rotated")    



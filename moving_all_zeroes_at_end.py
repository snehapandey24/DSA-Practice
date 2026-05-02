n = int(input("Enter size of the array"))
arr = []
non_zeroes = []
zeroes = []
for i in range(n):
    x = int(input("Enter the elements "))
    arr.append(x)

for i in range(n):
    if arr[i] != 0 :
        non_zeroes.append(arr[i])

for i in range(n) :       
    if arr[i] ==0:
        zeroes.append(0)

    
result = non_zeroes + zeroes
print(result)
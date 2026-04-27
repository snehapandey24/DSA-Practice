n = int(input("Enter the size of the array: "))
arr = []

largest = float("-inf")
second_largest = float("-inf")

for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)

for i in range(n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Largest =", largest)
print("Second Largest =", second_largest)

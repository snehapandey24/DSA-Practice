arr = [9,12,11,15,8]
target = 11
n = len(arr)
low =0
high = n-1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("found at index", mid)
        break
    elif target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1


             

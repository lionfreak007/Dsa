""" use partition to solve this
i/p - [0,1,0,1,0,0,1,1,1,0]
o/p-[0,0,0,0,0,1,1,1,1,1]

"""


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    print(low, " & ", high)

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def sort(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)

    sort(arr, low, p-1)
    sort(arr, p+1, high)


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
n = len(arr)
sort(arr, 0, n-1)
print("sorted array is:")
for i in range(n):
    print("%d" % arr[i])

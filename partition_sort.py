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
    print(arr)
    return i+1


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
n = len(arr)

partition(arr, 0, n-1)
print("sorted array is:")
for i in range(n):
    print("%d" % arr[i])

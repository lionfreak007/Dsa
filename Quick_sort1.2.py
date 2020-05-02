def Partition(arr, low, high):
    i = (low - 1)

    pivot = arr[high]
    print(low, "  ",  high)

    for j in range(low, high):

        if arr[j] < pivot:
            arr[i + 1], arr[j] = arr[j], arr[i + 1]

            i = i + 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(arr)

    return (i + 1)


def quickSort(arr, low, high):
    if low >= high:
        return
    p = Partition(arr, low, high)

    quickSort(arr, low, p-1)
    quickSort(arr, p+1, high)


arr = [10, 5, 3, 7, 1, 9, 4]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

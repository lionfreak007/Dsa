def Partition(low, mid, high):
    i = 0
    j = 0
    pivot = arr[high]

    for j in range(low, high-1):
        if arr[j] < pivot:
            arr[i + 1],arr[j] = arr[j],arr[i + 1]
            i = i + 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    p = Partition(arr, low, high)

    quickSort(arr, low, p-1)
    quickSort(arr, p-1, high)




arr = [10, 4, 7, 8, 1, 2] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
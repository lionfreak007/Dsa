def Partition(low,mid,high):
    i = low -1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j]< pivot:
            i =i + 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    p = Partition(arr, low, high)

    quickSort(arr, low, p-1)
    quickSort(arr, p-1, high)

def print_List(arr):
    for i in range(len.arr):
        print(arr[i] , end ='')
    print()


if __name__== '__main__':
    arr =[10, 20, 40, 30, 70, 60]

print("Unsorted array is: ")
print_List()

quickSort()

print("Sorted array is :")
print_List()



def merge_Sort(arr, L ,R):
    if (arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        

        first = 0
        second = 0
        third = 0

        while first <len(L) and second < len(R):
            if L[first] < R[second]:
                arr[third] = L[first]
                first = first + 1
            else:
                arr[third] = R[second]
                second = second + 1
            third = third + 1

        while first < len[L]:
            arr[third] = L[first]
            first = first + 1
            third = third + 1

        while second < len[R]:
            arr[third] = R[second]
            second = second + 1
            third = third + 1

    def print_List(arr):
        for i in range(len(arr)):
            print(arr[i] , end = '')
        print()

if __name__ == '__main__':
    arr = [10, 30, 20, 70, 50, 90]
    
    print("Unsorted array is : ")
    print_List(arr)

    merge_Sort()

    print( " sorted array is :")
    print_List(arr)



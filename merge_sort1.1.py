def merge_Sort(arr, L, R):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        first = 0
        second = 0
        third = 0

        while first < len(L) and second < len(R):

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

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    merge_Sort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


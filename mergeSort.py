# Python program for implementation of MergeSort
def mergeSort(arr):
    print("nilai arr ", arr)
    if len(arr) > 1:
        mid = len(arr) // 2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        print("L ", L)
        print("R ", R)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]

        print("arr sebelum di assign ", arr)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k += 1
        
        print("arr setelah di assign ", arr)

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):   
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for item in arr:
        # yield item
        print(item, end= " ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
            

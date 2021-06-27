def partition(A, low, high):
    pivot = A[low]
    i = low+1
    j = high
    
    while True:
        while i<=j and A[i]<=pivot:
            i+=1
        while i<=j and A[j]>=pivot:
            j-=1
        if i <= j:
            A[i], A[j] = A[j], A[i]       #swapping 
        else:
            break
        
    A[low], A[j] = A[j], A[low]
    return j

def Quick_Sort(A, low, high):
    if low<high:
        j = partition(A, low, high)
        Quick_Sort(A, low, j)
        Quick_Sort(A, j+1, high)
        
arr = list(map(int,input().split()))
Quick_Sort(arr, 0, len(arr) - 1)
print(arr)
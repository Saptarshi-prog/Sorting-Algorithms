A = list(map(int,input().split()))
n = len(A)

for i in range(n-1):
    j = k = i
    for j in range(i,n):
        if A[j]<A[k]:
            k = j
    t = A[i]            #swap(A[i], A[k])
    A[i] = A[k]
    A[k] = t
    
    
print("After selection sort, the sorted list is: ...")
print(A)

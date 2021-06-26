A = list(map(int,input().split()))
n = len(A)

for i in range(1,n):
    j = i-1
    x = A[i]
    while j>-1 and A[j]>x:
        A[j+1] = A[j]
        j-=1
    
    A[j+1] = x
    
print("After insertion sort, the sorted list is: ...")
print(A)
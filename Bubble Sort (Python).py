A = list(map(int,input().split()))
n = len(A)
flag = 1
for i in range(n-1):
    flag = 0
    for j in range(n-1-i):
        if A[j]>A[j+1]:
            t = A[j]
            A[j]=A[j+1]
            A[j+1] = t
            flag = 1
        
    if flag == 0:
        break
        
print("The sorted list is . . .")
print(A)

n = int(input())
arr = [int(i) for i in input().split()][:n]
c = 0
for i in range(0,n):
    if arr[i]%2==0:
        c+=1
print(c,len(arr)-c)
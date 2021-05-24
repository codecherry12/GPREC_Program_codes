n=10
arr1=[]
arr2=[]
for i in range(n):
    if i==0:
        arr2.append(40)
    else:
        arr2.append(arr2[i-1]+4)            
for i in range(n):
    if i==0:
        arr1.append(20)
    else:
        arr1.append(arr1[i-1]+arr2[i-1])

print(*arr1)
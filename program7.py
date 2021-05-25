n=int(input())
arr1=[]
for x in range(n):
    q=int(input())
    arr1.append(q)
i=0
sum=0
while i<len(arr1):
    for j in range(1,arr1[i]):
        if arr1[i]%j==0:
            x=j
            sum=sum+x
    if sum==arr1[i]:
        print('1')
    else:
        print('0')
    i+=1
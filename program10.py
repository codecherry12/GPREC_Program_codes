# You are using Python
n=int(input())
arr=list(map(int,input().split()))
sum=0
i=0
j=1
try:
    while i<len(arr) or j<4:
        x=arr[i]*j
        sum=sum+x
        i+=1
        j+=1
        if j>4:
            j=1
except:
    pass
if sum==1:
    print("yes")
else:
    print("no")
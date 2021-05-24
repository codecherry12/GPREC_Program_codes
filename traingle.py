# You are using Python
n=[int(x) for x in input().split()][:2]
z=0
for i in range(n[0],n[1]):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        
    if(count==4):
        z=z+1
print(z)
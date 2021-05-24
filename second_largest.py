n=10
slarge=0
for i in range(n):
    num=int(input())
    if(i==0):
        large=num
    elif (num>large):
        slarge=large
        large=num
    elif(num>slarge):
        slarge=num
print(slarge)   

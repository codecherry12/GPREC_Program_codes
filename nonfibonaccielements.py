n=10
a=0
b=1
c=0
while(c<=n):
    c=a+b
    a=b
    b=c
    d=a+b
    for x in range(c+1,d):
        if(x<=n):
            print(x,end =" ")
        else:
            break;
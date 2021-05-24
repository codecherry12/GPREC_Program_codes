# You are using Python
n1=int(input())
n2=int(input())
n3=int(input())
if(n1+n2+n3==180):
    if (n1==n2) and (n2==n3) and (n3==n1):
        print("Prize 3")
    elif n1==90 or n2== 90 or n3==90:
        print("Prize 2")
    else:
        print("Prize 1")
else:
    print("No Prize")
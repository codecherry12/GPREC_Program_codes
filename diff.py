# You are using Python
n=345

list1=[int(x) for x in str(n)]
if n>10:
    print(abs(list1[0]-list1[-1]))
else:
    print("Invalid Input")
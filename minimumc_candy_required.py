n=5
x="1 2 1 2 1"
y=x.split()
count=0
for i in range(n):
    if (y[i]==min(y)):
        count+=1
    else:
        count+=2
 
print(count)
    
curr = (100,50,10,5,1)

n = 576

count = 0
i = 0
rem = n

while rem!=0:
    count += rem//curr[i]
    rem = n % curr[i]
    i += 1

print(count)
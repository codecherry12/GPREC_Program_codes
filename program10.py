from itertools import combinations
N = int(input())

userinput = input()

num_list = userinput.split()

for i in range(0,N):
    num_list[i] = int(num_list[i])


quadlist = list(combinations(num_list, 4))



count = 0

for i in range(0,len(quadlist)):
    ans = sum(quadlist[i])
    if ans == 1:
        count = count + 1


if count > 0:
    print('YES')
else:
    print('NO')
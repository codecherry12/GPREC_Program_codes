"""Cookery Contest

Suzanne is participating in the Cookery Contest to be held at her Company. Suzanne is just a beginner in cooking but is more creative. She wanted to give a good show though she is going to cook for the first time. So she decided to cook only a small portion of her recipe, which has the same ratios of ingredients, but makes less food.

Suzanne however, does not like fractions. The original recipe contains only whole numbers of ingredients, and Suzanne wants the reduced recipe to only contain whole numbers of ingredients as well. Help her determine how much of each ingredient to use in order to make as little food as possible.

Input format
The first line of the input consists of a positive integer N, which corresponds to the number of ingredients.

Next line contains N space-separated integers, each indicating the quantity of a particular ingredient that is used.

Output format
Output exactly N space-separated integers on a line that gives the quantity of each ingredient that Suzanne should use in order to make as little food as possible.

Refer sample input and output for formatting specifications."""



n = 3
arr = [10,3,21]
print((arr))
ar1 = list(arr)
m=0
ar1.sort()
for i in range(0,n):
    if(ar1[i]!=0):
        m=ar1[i]
        break
s=0
while m!=0:
    for i in range(0,n):
        if arr[i]%m!=0:
            s=1
            break
    if(s==0):
        arr=[x//m for x in arr]
    m-=1
    s=0
print(*arr)
inp = [int(i) for i in input().split()][:3]
a,b,n=inp
a = a*(2**(n//2+n%2))
print(n//2+n%2)
b = b*(2**(n//2))
print(n//2)
print(a+b)
print(1//2,1%2)
arr = []
for i in range(0,3):
    x = input()
    arr.append(x)
print(arr)
print(arr.count(arr[0]))
if arr.count(arr[0])==3:
    print("Double Bonanza")
elif arr[0][0]==arr[1][0] and arr[1][0]==arr[2][0]:
    print("Bonanza")
elif arr[0][2]==arr[1][2] and arr[1][2]==arr[2][2]:
    print("Bonanza")
else:
    print("No Bonanza")
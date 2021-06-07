
l1=[1,2,3,4,5,6,7,8]
def arr(n):
    while n not in l1:
        for i in range(8):
            l1.append(l1[i]+8)
        del l1[:8]
    return l1
n=int(input())
arr(n)
l3=l1[:6]
l2=l1[6::]
dict2={l2[0]:str(l2[1])+'SU', l2[1]:str(l2[0])+'SL'}
dict1={l3[0]:str(l3[3])+'LB', 
      l3[1]:str(l3[4])+'MB',
      l3[2]:str(l3[5])+"UB",
      l3[3]:str(l3[0])+"LB",
      l3[4]:str(l3[1])+'MB',
      l3[5]:str(l3[2])+"UB"}
dict1.update(dict2)
print(dict1[n])
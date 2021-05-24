num = 1221
number=num
revnumber=0
while(num>0):
    rem=num%10
    revnumber = revnumber*10+rem
    num=num//10
print(num)
if(revnumber==number):
    print(number, "is palindrome" )
else:
    print(number, "is not palindrome")
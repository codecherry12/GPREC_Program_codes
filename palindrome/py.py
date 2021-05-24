# check wheather a given number is a palindrome ro not and print the next palindrome number

def reverse(n):
    rev = 0
    while n != 0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev
def ispalindrome(n):
    if(n==reverse(n)):
       
        return True
    else:
       
        return False

def nextpalindrome(n):
    while(not ispalindrome(n)):
        n+=1
    return n

print(reverse(123))
print(ispalindrome(123))
print(nextpalindrome(123))
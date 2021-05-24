#Function to check whether the 2 consecutive digits of a number's absolute difference is 1
def absdiff(input_list,N):
    flag = 'no'
    res = []
    
    for i in range (0,N):
        
        number = input_list[i]
        digit_list = digitlIST(number)
        for j in range(0,len(digit_list)-1):
            diff = digit_list[j] - digit_list[j+1]
            if abs(diff) == 1:
                flag = 'yes'
            else:
                flag = 'no'
                break

        if flag == 'yes':
            res.append(input_list[i])

    return res
            

#Function to get digits from a number            
def digitlIST(number):
    res_digit = [int(x) for x in str(number)]
    return res_digit
#main program    
N =200
input_list = []
for i in range (1,N+1):
    input_list.append(int(i))

res = absdiff(input_list,N)
if len(res) != 0:
    print(*res)
else:
    print('-1')



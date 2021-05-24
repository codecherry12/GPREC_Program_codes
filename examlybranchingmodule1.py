n = 5
import datetime
DOB_tot = "23 SEPTEMBER 1988 17 OCTOBER 1978 20 MAY 1980 23 APRIL 1987 22 JULY 1987"
dob = DOB_tot.split()
print(dob)
print(len(dob))

count = 0
endlimit = (n*3)-1
allowance_cust = []
for i in range(0,endlimit,3):
    count = count +1
    empdate = []
    
  
    empdate.append(dob[i])
    empdate.append(dob[i+1])
    empdate.append(dob[i+2])
    d1 = datetime.datetime(1987, 7, 22)
    if empdate[1] == 'JANUARY':
            month = 1
    elif empdate[1] == 'FEBRUARY':
            month = 2
    elif empdate[1] == 'MARCH':
            month = 3
    elif empdate[1] == 'APRIL':
            month = 4
    elif empdate[1] == 'MAY':
            month = 5
    elif empdate[1] == 'JUNE':
            month = 6
    elif empdate[1] == 'JULY':
            month = 7
    elif empdate[1] == 'AUGUST':
            month = 8
    elif empdate[1] == 'SEPTEMBER':
            month = 9
    elif empdate[1] == 'OCTOBER':
            month = 10
    elif empdate[1] == 'NOVEMBER':
            month = 11
    elif empdate[1] == 'DECEMBER':
            month = 12           
        
    d2 = datetime.datetime(int(empdate[2]),month,int(empdate[0]))
    
    if (d2 <= d1) and month in (1,3,5,7,8,10,12):
         allowance_cust.append(count)

if (len(allowance_cust)) == 0:
    print(-1)
else:
    print(*allowance_cust)
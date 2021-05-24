def find_num(x,y): # function with array and search element
    flag = 0 # intializing variable flag
    for item in x:
        if(item == y):
            flag+=1
    if(flag!=0):
        print(y,"is present "+str(flag)+" times")
    else:
        print(y,'is not present')
x=[1,1,3,1,1,3,5]
y=3
find_num(x,y)
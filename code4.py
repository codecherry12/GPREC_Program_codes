"""give an array and return second largest even number"""
def get_Second_Largest_Even_number(arr):
    largest_even_number = arr[0]
    second_largest_even = arr[0]
    
    for num in arr:
        if(num % 2 == 0):
            if(num > largest_even_number):
                second_largest_even = largest_even_number
                largest_even_number = num
            elif(num>second_largest_even):
                second_largest_even = num
    return second_largest_even

arr = [14,46,47,86,93,52,48,36,66,85]
print(get_Second_Largest_Even_number(arr))
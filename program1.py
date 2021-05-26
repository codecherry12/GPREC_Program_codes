N = int(input())
rating = input()
rating_list = rating.split()

for i in range (0,N):
    rating_list[i] = int(rating_list[i])

candies = 0


#function to get unique values 
def unique(list1): 
      
    # insert the list to the set 
    list_set = set(list1)
    # convert the set to the list 
    unique_list = (list(list_set))
    return unique_list


unique_list = unique(rating_list)

unique_list.sort()

for i in range(0,N):
    candies = candies + (unique_list.index(rating_list[i]))+ 1

print(int(candies))
nums = [1,2,3,4,5,6,7,8,9,10]

# filter(function,list)
def even(num):
    return (num%2) == 0
# print(filter(even,nums))
# print(list(filter(even,nums)))

evenNums = list(filter(even,nums)) 
print(evenNums)

#map and filter are the same functions but usage of map is 'to change all of each item in list' and filter is 'to change some item in list'


#comprehension
nums =[num for num in nums if (num%2)==0]
print(nums)


#for loop
evenNums = []
for num in nums :
    if (num%2) == 0 :
        # print(num)
        evenNums.append(num)
        
print(evenNums)
nums = [2,4,6,7,23,53,73]

# map(function,list)
def mapFunction(num):
    return num*2

num = list(map(mapFunction, nums))
print(num)

nums = [num*2 for num in nums]#comprehension
print(nums)
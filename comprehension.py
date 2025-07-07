prices = [200,4300,620,4000,1020]

doouble_prices = []
for price in prices :
    # print(price*2)
    doouble_prices.append(price*2)
print(doouble_prices)


doouble_prices = [price*2 for price in prices] #comprehensive
print(doouble_prices)


nums = [1,2,3,4,5,6,7,8,9,10]
even_double_nums = []
for num in nums :
    if (num%2) == 0 :
        # print(num*2)
        even_double_nums.append(num*2)
print(even_double_nums)


even_double_nums = [num*2 for num in nums if (num%2) == 0] #logic , from where , condition
print(even_double_nums)
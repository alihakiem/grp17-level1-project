shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
sum = 0

for item, price in shopping_cart_dict.items():
    shopping_cart_dict[item] = price + price * 10/100
    sum = sum + shopping_cart_dict[item]

print('raise = ', shopping_cart_dict)
print('sum = ', sum)

net_value = sum + sum * 14/100
print( net_value)



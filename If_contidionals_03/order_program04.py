#program to get order discount
#inputs :
item_cost = 500
item_qty = 3
special_client = 1
#-----------------------------
total_order_cost = item_cost * item_qty
if(total_order_cost >= 1000):
    if special_client >0:
        discount_pct = 20
    else:
        discount_pct = 10
else:
    discount_pct = 0
print('total order cost = ' , total_order_cost)
print('discount percentage = ' , discount_pct)
discount_val = discount_pct/100 * total_order_cost
print('discount value = ', discount_val)
total_order_cost = total_order_cost-discount_val
print('the final total order cost =' , total_order_cost)
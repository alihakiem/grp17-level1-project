#program to get sum , count of +ve , -ve numbers and count of zeroes in a list
number_list = [14, 5, -2, 20, -3, -7, 0, 4, 0]
sum_pos, count_pos, sum_neg, count_neg, count_zeroes = 0,0,0,0,0
for item in number_list:
    if item > 0 :
        sum_pos = sum_pos +item
        count_pos = count_pos+1
    elif item < 0:
        sum_neg = sum_neg + item
        count_neg = count_neg+ 1
    else:
        count_zeroes = count_zeroes+1

print('Sum pos = ', sum_pos, 'Sum neg = ', sum_neg, 'count pos = ' ,count_pos, "count neg = ", count_neg,
"count zeroes" , count_zeroes)

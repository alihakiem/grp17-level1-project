from datetime import datetime
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
chosen_month = dates_list[0].month
check = 0
for date in dates_list:
    if date.month == chosen_month:
        check = check+1

if len(dates_list) == check:
    print(f"All dates are in the same month : {chosen_month}")
else:
    print("not all are in the same month")

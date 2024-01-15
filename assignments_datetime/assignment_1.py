from datetime import datetime
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
oldest_date = dates_list[0]
for date in dates_list:
    if date < oldest_date:
        oldest_date = date

print(oldest_date.strftime("%Y-%m-%d"))

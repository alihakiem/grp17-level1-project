from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)
counter = 0
for date in dates_list:
    if date == given_date:
        counter = counter + 1
print(f"{given_date.date()} occurs {counter} times")

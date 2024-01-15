from datetime import datetime
from dateutil import relativedelta
given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
try:
    index = dates_list.index(given_date)
    print(f"{given_date.strftime('%d-%m-%Y')} is found in the list at index {index}")
except ValueError:
    print("The date is not found in the list.")


#Get the difference between 2 date in days as a total
from datetime import datetime
from dateutil import relativedelta
today = datetime.now()
custom_date = datetime(1,2,20)

difference_in_day = today - custom_date
print(difference_in_day)
print(difference_in_day.days)

print("using relative delta class; to get difference---")
difference_parts = relativedelta.relativedelta(today, custom_date)
print(difference_parts)
print(f"years = {difference_parts.years}, months = {difference_parts.months}"
      f", days = {difference_parts.days}")

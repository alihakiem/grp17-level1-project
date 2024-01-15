from datetime import datetime
from dateutil import relativedelta
year = 2023
month = 11
custom_date = datetime(year,month,1)
end_date = custom_date + relativedelta.relativedelta(months=1)
weekend_counters = 0
print(custom_date,custom_date.date().weekday())


while custom_date < end_date:
    if custom_date.weekday() in [4,5]:
        weekend_counters = weekend_counters+1
    custom_date = custom_date + relativedelta.relativedelta(days = 1)
print(f"the number of weekends {weekend_counters}")

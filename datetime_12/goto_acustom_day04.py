from datetime import datetime
from dateutil import relativedelta

today = datetime.now()

print("--Get to the first day in this month---")
first_day = today + relativedelta.relativedelta(day=1)
print(first_day)
print("---Get to the last day in this month")
last_day = today+ relativedelta.relativedelta(day=31)
print(last_day)

from datetime import datetime
from dateutil import relativedelta
start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)
current_date =start_range
targeted_dates =[]
while end_range>=current_date:
    targeted_dates.append(current_date.date())
    current_date=current_date +relativedelta.relativedelta(days=1)

print(targeted_dates)

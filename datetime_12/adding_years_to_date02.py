from datetime import datetime
from dateutil import relativedelta
today = datetime.now()
print(today)

#new_date = today + 5 Error :should use relative delte
new_date = today + relativedelta.relativedelta(years=0,months=5,days=5)
print(new_date.date())
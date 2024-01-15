#program to show the nearest sundays
import calendar
from datetime import datetime
from dateutil import relativedelta
today = datetime.now()
print("-------the nearest sunday from today-------")
nearest_sunday = today + relativedelta.relativedelta(weekday=calendar.SUNDAY, weeks=1)
print(nearest_sunday)
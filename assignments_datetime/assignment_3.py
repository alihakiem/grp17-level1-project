from datetime import datetime
from dateutil import relativedelta
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if given_date < end_date and given_date > start_date:
    print("The date is in range")
else:
    print("The date is not in range")
from datetime import datetime
print("get the current date and time")
today = datetime.now()
print(today)
print("get only date or time or their parts")
print(today.date())
print(today.date().year)
print(today.date().month)
print(today.date().day)
print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('-----------Re formatting date,time---| we use strftime() function-------------')
print('---convert date into string using strftime() function----')
print(today.strftime("%d-%m-%Y-%w "))# %w ---> means weekday
print(today.strftime("%B-%b-%A-%a")) #Month, Mon, day, Dy
print(today.strftime("%H-%M-%S"))#Hours in 24 style
print(today.strftime("%I-%M-%S-%p"))#Hours in 24 style

print("---------Create a custom date :24-04-2023----------")
print("---1st way : datetime object using constructor()------")
custom_date = datetime(2023,12,25,12,15,20)
print(custom_date)

print('----2nd way - by converting a string to Date-------')
date_style_string = "24-4-2023"
new_custom_date = datetime.strptime(date_style_string,'%d-%m-%Y')
print(new_custom_date.date())
print(new_custom_date.strftime("%d-%m-%Y"))

print("----------Comparison-------------")
if today.date() >custom_date.date():
    print("Today is newer than custom date")
elif today.date() < custom_date.date():
    print("today is older than custom date")
else:
    print("2 dates are equal")

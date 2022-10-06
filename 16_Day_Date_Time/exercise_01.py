from datetime import datetime
from time import time
# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
timestamp = now.timestamp()
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
format_current_time = now.strftime('%m/%d/%Y, %H:%M:%S')
print(format_current_time)
# Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
date_time = datetime.strptime(today, '%d %B, %Y')
print(date_time)
# Calculate the time difference between now and new year.
t1 = datetime.now()
t2 = datetime(year=2023, month=1, day=1)
diff = t2 - t1
print(diff)
# Calculate the time difference between 1 January 1970 and now.
t1 = datetime.now()
t2 = datetime(year=1970, month=1, day=1)
diff = t1 - t2
print(diff)

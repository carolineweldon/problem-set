from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
x = now.strftime("%A, %B %d %Y %Z at %H:%M:%S")
print(x)
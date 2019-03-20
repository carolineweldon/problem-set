import datetime 

today = datetime.datetime.today().weekday()
if today == 1 or 3:
  print("Yes, today does begin with a T")
else:
  print("No, today does not begin with a T")





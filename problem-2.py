#Caroline Weldon 
#Program to test if current day start with a T
#import datetime- inbuilt module in python 
import datetime 
#set current day as today- value which is represented as numeric 0-6 
today = datetime.datetime.today().weekday()
#if today is tueday/1 or thursday/3
if today == 1 or 3:
  print("Yes, today does begin with a T")
else:
  print("No, today does not begin with a T")





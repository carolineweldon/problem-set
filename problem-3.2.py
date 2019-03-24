#Caroline Weldon 
#Program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12
#assign x to list of numbers between 1000 and 10000
x = list(range(1000, 10000))
#test all numbers in list x;if they can divided by 6 but not by 12
for num in x:
     if num % 6 == 0 and num % 12 != 0:
         #print num
          print(num)
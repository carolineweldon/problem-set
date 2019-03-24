#Caroline Weldon 
#Program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

#assign numbers in range 1000 to 10000 divisible by 6 but not 12 to list 
list = [ x for x in range(1000, 10000) if x % 6 == 0 and x % 12 != 0  ]

print(list)
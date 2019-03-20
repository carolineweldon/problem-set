#Prompt user to input a positive integer and assign this input to i
i = int(input("enter a positive integer:"))

#create Total which is the sum of the range of numbers between 1 and i 
#note we use i+1 as range always starts on value 0 for first number in the range
Total = sum(range(1, i+1))

#print this calculation 

print(Total)
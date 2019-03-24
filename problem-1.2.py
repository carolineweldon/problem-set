#Caroline Weldon 
#Ask user to input any positive integer and outputs the sum of all numbers between one and that number.

#user input a number and assign this to n
n = int(input("enter a positive integer:"))

ans = 0
i = 1
#while loop sums all numbers from 1 to n and stores in ans
while i <= n:
  ans = ans + i
  i = i + 1

print(ans)
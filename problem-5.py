
i = int(input("Enter a positive number: "))

if i > 1:
   
   for x in range(2,i):
       if (i % x) == 0:
           print(i,"is not a prime number")
           break
   else:
       print(i,"is a prime number")
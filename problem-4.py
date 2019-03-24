#Caroline Weldon
#User prompted to enter a value.Calculate the next value by taking the current value and, if it is even, divide it by two,
#but if it is odd, multiply it by three and add one. End at 1

i = int(input("enter a positive integer:"))
while i != 1:

        if i % 2 == 0:
            i = (i//2)
            print(i)
            

        elif i % 2 == 1:
            i = (3*i+1) 
            print(i)
            
        

        

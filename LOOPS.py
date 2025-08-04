#Print 1 to 10
'''i=1
while i<=10:
    print(i)
    i=i+1'''

#Print a number to 1 each value
'''num=int(input("enter the number"))
while num>=1:
    print(num)
    num=num-1'''

#Sum of even numbers from 1 to 100
'''S=0
i=1
while i<=100:
    if i%2==0:
        S=S+i
    i+=1
print(S)'''

#Random number guessing game
import random
num=random.randint(1,10)
guess=False
while (guess==False):
    Guess=int(input("enter the number between 1 to 10"))
    if Guess>num:
        print("too high")
    elif Guess<num:
        print("too low")
    else:
        print("yours guess is correct")
        guess=True
    

#print factorial of a number
'''num=int(input("enter the number"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i=i+1
print(fact)'''

#sum of digits of a given integer

    
    
    
    



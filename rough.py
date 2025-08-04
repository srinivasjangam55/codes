#program for printing the sum of even digits in a given number
'''num=int(input("enter the number"))
S=0
while num>=1:
    remainder=num%10
    if remainder%2==0:
        S=S+remainder 

    num=num//10
print(S)'''

#Sum of divisors of a number
num=int(input('enter the given number'))
d=1
S=0
while d<=num:
    if num%d==0:
        S=S+d
        
    d=d+1
print(S)
    
    
        
    

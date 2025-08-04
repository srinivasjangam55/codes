#Cnt the number of even digits in a number
'''num=int(input("enter the number"))
cnt=0
while num>0:
    t=num%10
    if t%2==0:
        cnt=cnt+1
    num=num//10
print(cnt)'''

#Print square numbers from 1 to 10
'''i=1
while i<=10:
    print(i**2,end=" ")
    i=i+1'''

#Find GCD among the two numbers
'''a=int(input("enter a number"))
b=int(input("enter another number"))
if a<b:
    small=a
else:
    small=b
n=small
while n>1:
    if a%n==0 and b%n==0:
        print("GCD is",n)
        break
    n=n-1
else:
    print("No GCD")'''

#find left most digit of a number
num=int(input("enter the number"))
while num>9:
    num=num//10
print(num)

        



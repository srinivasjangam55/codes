#Sum of all elements in a given list
'''lst=[1,2,3,4,5]
S=0
for i in lst:
    S=S+i
print(S)'''

#largest number in a given list
'''l=list(map(int, input("enter list elements").split(",")))
large=float('-inf')
for i in l:
    if i>large:
        large=i
print(large)'''

#Write a Python program to find the smallest number from a given list of integers using a for loop.
'''l=list(map(int, input("enter list elements").split(",")))
small=float('+inf')
for i in l:
    if i<small:
        small=i
print(small)'''

#Write a Python program to check whether a given element exists in a list or not.
'''lst=[1,2,3,4,5,7,8]
element=int(input("enter a element:"))
if element in lst:
    print("yes")
else:
    print("not in lst")'''

#prime
'''for any prime
no we wont have any factor
from 2 to sqrt n.
other than 2 3 every prime can
be written as 6*i+-1 but it may
or may not be prime'''
n=int(input())
f=0
if n==1:
    print(n," is neither prime nor composite")
for i in range(2,int(n**.5)+1):
    if n%i==0:
        f=1
        break
if f==0 and n!=1:
    print(n," prime")
elif f==1 and n!=1:
    print(n," composite")

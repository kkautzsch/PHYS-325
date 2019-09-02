#!/usr/bin/env python3 

#import math   #no longer needed, because we implement our function manually now

# this promts to enter a positive number
data = input("Enter a positive number: ")
data2=int(data)

def f(n):
    """return Fibonacci series up to n."""
    
    # this checks if the number is positive
    if n<0:
        print("Sorry, the number must be positive")
    # this checks if the number is positive
    else:
        if n == 0:
            return 1
        else:
            x=1	# x is the factorial of the input number
            for l in range(n):
                x*=l+1
            return x 

#old version of f(n)
'''
def f(n): re
    return math.factorial(n)
'''

# this checks if the number is positive
if data2<0:
    print("Sorry, the number must be positive"); print("Enter a different number next time, please")
# this checks if the number is positive
elif data2<-5: print("Sorry the number is too small"); ptint("Enter a different number next time, please")
# this checks if the number is positive
else:
    print("The factorial of ",data2," is ",f(data2))
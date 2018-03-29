"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here

def proizvod (a,b):
    pr=a*b
    return pr
pr=proizvod(2,4)
print(pr)


# function to count number of digits
# in the product of two numbers
def countDigits(a, b):
    count = 0

    # absolute value of the
    # product of two numbers
    p = abs(a * b)

    # if product is 0
    if (p == 0):
        return 1

    # count number of digits
    # in the product 'p'
    while (p > 0):
        count = count + 1
        p = p // 10

    # required count of digits
    return count


a = 33
b = -24
print("Number of digits = ",
      countDigits(a, b))



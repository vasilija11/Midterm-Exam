"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

#Poluprecnik kruga je P=r**2*pi
#pi iznosi 3.14159

import math

def povrsina_kruga(poluprecnik):

    if (not isinstance(poluprecnik, int)) and (not isinstance(poluprecnik, float)): # unijeti broj mora biti cijeli ili decimalni, pa to ispitujemo,
                                                                                    #ako nije vraca -1
        return -1

    return (abs(poluprecnik)**2)*math.pi


def main():

    povrsina=povrsina_kruga(2.4)
    print("Povrsina je: ", povrsina)

    pass

main()
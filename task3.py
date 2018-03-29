"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
*Negative and Non-Negative Elements
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here
broj_elemenata_niza= int(input("Unesite broj elemenata niza: "))
niz= []
negativni= 0
nenegativni= 0
for i in range(broj_elemenata_niza):

    element_niza= input("Unesite novi element: ")
    niz.append(element_niza)
    
    print(niz)
    print(negativni)
    print(nenegativni)
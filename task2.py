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

broj = eval(input("Unesi cijeli broj: ")) # eval procjenjuje sta je korisnik unio

if not isinstance(broj,int): # ispitujemo da li je unijeti broj cio broj
    print("Pogresan unos!")
    quit()

product = 1

for i in str(abs(broj)): # prolazi kroz cifre datog broja(ali apsolutnog, zbog minusa)

    product *= int(i) # mnozi sve cifre datog broja


if broj < 0: #ako je br negativan proizvod cifri ce mu takodje biti negativan, pa zato dobijeni proizvod mnozimo na kraju sa -1

    print("Proizvod cifri datog broja iznosi: ", (-1) * product)

else:
    print("Proizvod cifri datog broja iznosi: ", product)
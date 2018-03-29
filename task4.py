"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here



string = input("Enter any string to convert in uppercase: ");
if string == 'x':
    exit();
else:
    string_in_uppercase = string.upper();
    print("\nString in Uppercase =",string_in_uppercase);

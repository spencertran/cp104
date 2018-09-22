"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Tran
ID:      180565470
Email:   tran5470@mylaurier.ca
__updated__ = "2018-09-18"
-------------------------------------------------------
"""
# Imports

# Constants
cost = float(input('What is the cost of 1 pizza? $'))
amount = int(input('How many pizzas would you like to order?'))
total = cost * amount
print()
print('Total cost of' , amount , 'pizzas:' ,'${:.2f}' .format(total))
 
def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
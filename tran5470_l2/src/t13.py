"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Tran
ID:      180565470
Email:   tran5470@mylaurier.ca
__updated__ = "2018-09-16"
-------------------------------------------------------
"""
# Imports

# Constants

amount_seconds = (int(input('Enter number of seconds:' )))
amount_in_hour = 3600
hours = amount_seconds//amount_in_hour
minutes = (amount_seconds//hours) - (hours * 60)
seconds = amount_seconds % 60
print('There are {} hours, {} minutes, and {} seconds in {} seconds'.format(hours, minutes, seconds,amount_seconds) )

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
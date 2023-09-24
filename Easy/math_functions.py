###########################################################
############### Some easy functions to start###############
###########################################################

def add_numbers(a, b):
    return a + b

def factorial(n):
    """
    Function to perform factorial operations. eg:
    0! = 1 (by convention, the factorial of 0 is defined to be 1).
    1! = 1 (since there is only one positive integer from 1 to 1).
    2! = 2 x 1 = 2.
    3! = 3 x 2 x 1 = 6.
    4! = 4 x 3 x 2 x 1 = 24.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

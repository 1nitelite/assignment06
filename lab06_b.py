"""
Title: SoC.py
Desc: Script demonstrating Function concept, based on Basic_Math.py (Assignment02)
Change Log: (Who, When, What)
NToulas, 2022-May-25, Created File>
"""

# -- DATA -- #
intNumA = None
intNumB = None

# -- PROCESSING -- #
# Process the data
def doMath(x, y):
    c = x + y
    d = x - y
    e = x * y
    f = x / y
    result = 'Sum:\t\t {}\nDifference:\t {}\nProduct:\t {}\nQuotient:\t {} '.format(c, d, e, f)
    return result

# -- PRESENTATION (Input/Output) -- #
# Get User input data
print('Basic Math script. Calculating the Sum, Difference, Product, and Quotient of two numbers.')
intNumA = int(input('Please enter the 1st number: '))
intNumB = int(input('Please enter the 2nd number: '))
# Display the Results
print('\n\nThis script calculated using the Numbers', intNumA, 'and', intNumB)
print('The Results are:\n')
# print('Sum:\t\t', getSum(), '\nDifference:\t', getDif())
# print('Product:\t', getPro(), '\nQuotient:\t', getQuo())
print(doMath(intNumA, intNumB))
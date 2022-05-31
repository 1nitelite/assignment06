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
class SimpleMath:
    """
    The SimpleMath class contains a group of functions that does simple math operations.
    """

    def getSum():
        """
        The getSum function adds two numbers and returns the sum.
        :param first: the first number to be added
        :param second: the second number to be added
        :return: The sum of the two parameters
        """
        sum = intNumA + intNumB
        return sum

    def getDifference():
        """
        The getDifference function subtracts one number from the other and returns the difference.
        :param first: the number to be subtracted from (minuend)
        :param second: the number to be subtracted (subtrahend)
        :return: The difference of the parameters
        """
        difference = intNumA - intNumB
        return difference

    def getProduct():
        """
        The getProduct function multiplies two numbers and returns the product.
        :param first: the first number to be multiplied
        :param second: the second number to be multiplied
        :return: The product of the two parameters
        """
        product = intNumA * intNumB
        return product

    def getQuotient():
        """
        The getQuotient function divides two numbers and returns the quotient.
        :param first: the number to be divided from (dividend)
        :param second: the number to be divided (divisor)
        :return: The quotient of the two parameters
        """
        quotient = intNumA / intNumB
        return quotient

# -- PRESENTATION (Input/Output) -- #
# Get User input data
print('Basic Math script. Calculating the Sum, Difference, Product, and Quotient of two numbers.')
intNumA = int(input('Please enter the 1st number: '))
intNumB = int(input('Please enter the 2nd number: '))
# Display the Results
print('\n\nThis script calculated using the Numbers', intNumA, 'and', intNumB)
print('The Results are:\n')
print('Sum:\t\t', SimpleMath.getSum(), '\nDifference:\t', SimpleMath.getDifference())
print('Product:\t', SimpleMath.getProduct(), '\nQuotient:\t', SimpleMath.getQuotient())
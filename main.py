# def multiply(a, b):
#     product = a * b
#     return product
#
# product = multiply(324, 456)
# print(product)

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def product(a, b):
        product = 0
        for i in range(a):
            product = Calculator.add(product, b)
        return product

class Geometry:
    @staticmethod
    def area_of_square(a):
        area = Calculator.product(a, a)
        return area

print(Geometry.area_of_square(4))


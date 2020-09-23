# Factorial

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Factorial:
    def __init__(self):
        self.number = -1
        self.factorial = 0

    def getNumber(self):
        self.number = int(input('Enter an integer number > '))

    def getFactorial(self, number):
        if number == 0:
            self.factorial = 1
        else:
            # self.factorial = number * getFactorial(number - 1) <-- This cannot be used in Python
            self.factorial = 1
            for i in range(1, number+1):
                self.factorial = self.factorial * i

# Press the green button in the gutter to run the script.

fct = Factorial()
while(fct.number < 0):
    fct.getNumber()
    if fct.number < 0:
        print('**Error: Number mustn\'t be negative.')
    elif fct.number > 20:
        print('**Error: Number is too large.')

num = fct.number
fct.getFactorial(num)
print('{0}! = {1}'.format(num, fct.factorial))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

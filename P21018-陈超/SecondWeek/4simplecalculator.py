class Calculator(object):
    """
    A simple calculate tool.
    """

    @staticmethod
    def pre_calculate():
        global n1, symbol, n2
        while True:
            try:
                n1 = int(input("Enter first number:\n>>>"))
                symbol = str(input("Enter a arithmetic symbol: \n+, -, *, /\n>>>")).strip()
                if symbol not in ['+', '-', '*', '/']:
                    print("Input symbol is not contained of arithmetic symbol.")
                    continue
                n2 = int(input("Enter second number:\n>>>"))
            except ValueError:
                print("The input Value is Wrong type, Please try again.")
                continue
            return n1, symbol, n2

    @staticmethod
    def calculate(three_tuple):
        global calc_res
        number1 = three_tuple[0]
        sybl = three_tuple[1]
        number2 = three_tuple[2]

        if sybl == '+':
            calc_res = number1 + number2
        elif sybl == '-':
            calc_res = number1 - number2
        elif sybl == '*':
            calc_res = number1 * number2
        elif sybl == '/':
            try:
                calc_res = number1 / number2
            except ZeroDivisionError:
                print("Reason: The divisor in division can't be zero.\nDirect cause: the second number is zero")
        return "The calculate result: {}".format(calc_res)


if __name__ == '__main__':
    loop_time = 1

    while True:
        calc = Calculator()
        print("\nCalculate times: {}".format(loop_time))
        pre_calc = calc.pre_calculate()
        try:
            result = calc.calculate(pre_calc)
            print("{} {} {}".format('*' * 20, result, '*' * 20), sep="\n")
        except NameError:
            print("Reason: calc_res.\nDirect Cause: calc.pre_calculate have a ValueError")
        loop_time += 1

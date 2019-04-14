while True:
    num1 = str(input('please input number one:'))
    while num1.isdigit():
        num1=int(num1)
        operator = (input('please input one operator + or  -  ro *  or /:'))
        operator1 = ['+','-','*','/']
        if operator in operator1:
            num2 = str(input('please input number two:'))
            if num2.isdigit():  
                num2=int(num2)
                if operator == '+':
                    print('{} + {} = {}'.format(num1,num2,num1+ num2))
                    break
                elif operator == '-':
                    print('{} - {} = {}'.format(num1,num2,num1-num2))
                    break
                elif operator == '*':
                    print('{} * {} = {}'.format(num1,num2,num1*num2))
                    break
                else:
                    print('{} / {} = {}'.format(num1,num2,num1/num2))
                    break
        num2=str(num2)
        num1=str(num1)
    continue

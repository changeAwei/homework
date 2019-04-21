operator = ['+', '-', '*', '/']
flag =False
while not flag:
    num_1 = input("Please enter a number:")
    if num_1.strip().isdigit() == False:
        continue
    while not flag:
        opr = input('Please enter an operator (+-*/):')
        if opr not in operator:
            continue 
        else:
            while not flag:
                num_2 = input("Please enter a number again:")
                if num_2.strip().isdigit() == False:
                    continue
                if opr == '+':
                    print('Result:', int(num_1) + int(num_2))
                elif opr == '-':
                    print('Result:', int(num_1) - int(num_2))
                elif opr == '*':
                    print('Result:', int(num_1) * int(num_2))
                elif opr == '/':
                    print('Result:', int(num_1) / int(num_2))
                break
        quit = input("Enter 'q' to exit and any other key to continue.:")
        if quit == 'q':
            flag = True
        else:
            break












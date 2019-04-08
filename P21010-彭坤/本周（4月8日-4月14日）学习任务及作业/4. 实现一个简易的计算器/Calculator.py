operator = ['+', '-', '*', '/']
flag =False
while not flag:
    num_1 = input("Please enter a number:").strip()
    if num_1.isdigit() == False:
        continue
    
    while not flag:
        opr = input('Please enter an operator (+-*/):').strip()
        if ''.join(operator).find(opr) == -1:
            continue 
        else:
            while not flag:
                num_2 = input("Please enter a number again:").strip()
                if num_1.isdigit() == False:
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
        quit = input("Enter 'q' to exit and any other key to continue.:").strip()
        if quit == 'q':
            flag = True
        else:
            break












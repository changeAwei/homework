q = 1
while q:
	num1 = int(input('please input a number:'))
	ope = input('please a operator(+ - * /):')
	num2 = int(input('please input a number:'))
	if ope == '+':
		print('{}+{}={}'.format(num1, num2, num1 + num2))
	elif ope == '-':
		print('{}-{}={}'.format(num1, num2, num1 + num2))
	elif ope == '*':
		print('{}*{}={}'.format(num1, num2, num1 * num2))
	elif ope == '/':
		print('{}/{}={}'.format(num1, num2, num1 + num2))
	else:
		print('calculation failure')
		continue
	q = int(input("Enter '0' to exit, Enter '1' to continue"))


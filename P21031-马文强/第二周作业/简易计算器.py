while True:
    n = int(input('please input number'))
    oper = input('please input "+", "-", "*", "/"')
    m = int(input('please input number'))
    #if input('please input number') == ' ':  ���ﲻ֪��Ϊʲôû�г����ж϶��ǳ����������ϣ����ʦ���һ��
        #break
    if oper == '+':
        print(n + m)
    elif oper == '-':
        print(n - m)
    elif oper == '*':
        print(n * m)
    elif oper == '/':
        print(n / m) 
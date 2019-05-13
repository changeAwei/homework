
def calulate(fnum,operator,snum):
    if operator == '+':
        return fnum + snum
    elif operator == '-':
        return fnum - snum
    elif operator == '*':
        return fnum * snum
    elif operator == '/':
        return fnum / snum

def isnum(num):      #验证用户输入的是否为数字
    while True:
        if num.isdigit() or num == 'q':
            return num
        else:
            num =   input("wrong input ,please retry >>")
            num = num.lstrip('0') if num.lstrip('0') else '0'

def getfnum():
    f_num = input('please input  first num>>:').strip()
    f_num = f_num.lstrip('0') if f_num.lstrip('0') else '0'
    return isnum(f_num)


def getopera():
    opera = input("please input opeartor >>:").strip()
    while opera not in ['+', '-', '*', '/']:
        opera = input("wrong input , opeartor must in  ['+','-','*','/']>>:").strip()
        return opera
    return  opera

def getsnum(opera):
    s_num = input('please input second num>>:').strip()
    s_num = s_num.lstrip('0') if s_num.lstrip('0') else '0'
    if s_num == '0' and opera == '/':
         print('division by zero')
         return 'continue'
    return isnum(s_num)

def playtimes(n):
    if n !=0:
        strs = 'you have played {} times,input "q" to exit>>'.format(n)
        newinput = input(strs)
        return newinput

print("welcome to calculate,if you want to quit, press 'q' anywhere!")
isquit = True
n = 0
while isquit:
    if playtimes(n) == 'q': break
    fnum = getfnum()
    if fnum == 'q' : break
    opera = getopera()
    if opera == 'q': break
    snum = getsnum(opera)
    if snum == 'q': break
    if snum == 'continue': continue
    result = calulate(int(fnum), opera, int(snum))
    n =+ 1
    print('the result is {} '.format(result))

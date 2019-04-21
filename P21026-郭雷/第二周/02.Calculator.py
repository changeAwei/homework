
####4. 实现一个简易的计算器，效果如下：
##    （1）. 运行后提示让用户输入一个数字
##    （2）. 提示输入操作符（+ - * /）
##    （3）. 再次提示输入一个数字
##    （4）. 打印计算结果
##    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
#输入一个数字，若输入的是非数字，请再次输入，并在最后输出错误次数
listcac =["+", "-","*", "/"]
def my_input():
    flag=False
#    n=0
    while  not flag:
            a=input('请输入数字>>')#输入数据
            flag=a.isdigit() #类型转换
            if  not flag:
                print('输入错误，请再次输入数字')

#                n+=1#统计输入错误的次数
            else:
                print("The  input  is ",a)
#                print("The times about erro  is ",n)
    return int(a);



def my_cac():
    flag=False
#    n=0
    while  not flag:
            a=input('输入操作符（+ - * /）>>')#输入数据
            flag=(a in listcac)#判断运算符是否正确
            
            if  not flag:
                print('输入错误，请再次输入数字')
#                n+=1#统计输入错误的次数
            else:
                print("The  input  is ",a)
#                print("The times about erro  is ",n)
                
    return listcac.index(a);
def my_print():
    if cac==0:
        print (a,"+",b,"=",a+b)
    elif cac==1:
        print (a,"-",b,"=",a-b)
    elif cac==2:
        print (
            a,"*",b,"=",a*b)
    else:
            if b==0:
                print("除数不能为零")
            else:
                print (a,"/",b,"=",float(a/b)) 
my_flag=True

while my_flag:
    a=my_input()
    cac=my_cac()
    b=my_input()
    my_print()
    my_quit=input("继续计算请点击任意按钮,退出请输入q or Q")
    if (my_quit == "q" or my_quit == "Q" ):
        my_flag=False
 

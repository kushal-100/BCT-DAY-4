import cal
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
operation1=input("choose the operation 1.+ \n 2.- \n 3.* \n 4./ \n")
if operation1=='1':
    a=cal.add(num1,num2)
    print(a)
elif operation1=='2':
    a=cal.sub(num1,num2)
    print(a)
elif operation1=='3':
    a=cal.mul(num1,num2)
    print(a)
elif operation1=='4':
    a=cal.div(num1,num2)
    print(a)    
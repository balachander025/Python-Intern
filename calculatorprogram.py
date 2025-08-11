num1=int(input("Enter the number1"))
operator=input("Enter operator(+,-,*,/)")
num2=int(input("Enter the number2"))

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
        result=num1/num2
    else:
        print("The Number is Zero")

else:
    print("The number is Not perform  Any operations")

print("Result",result)




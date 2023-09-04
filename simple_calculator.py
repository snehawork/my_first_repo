first_number=int(input("enter the first number:"))
second_number=int(input("enter the second number"))
operator=input("enter the operator:")
if(operator=='+'):
    a=first_number+second_number
    print("Addition of 2 nos is :",a)
elif operator=='-':
    b=first_number-second_number
    print("subtraction of 2 nos is:",b)
elif operator=='/':
    c=first_number/second_number
    print("division of 2 nos is:",c)
elif operator=='*':
    d=first_number*second_number
    print("multiplication of 2 nos is:",d)
else:
    print("its not a valid operator")





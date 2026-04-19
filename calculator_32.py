a = int(input("enter a : "))
b = int(input("enter b : "))
x = str(input("enter a operator : "))
match x :
    case '+':
        print("addition of a & b ",a+b)
    case '-':
        print("subtraction of a & b ",a-b)
    case '*':
        print("multiplication of a & b ",a*b)
    case '/':
        print("division of a & b ",a/b)
    case '%':
        print("floor of a & b ",a%b)
    case '//':
        print("modulus of a & b ",a//b)
    case '**':
        print("exponention of a & b ",a**b)    


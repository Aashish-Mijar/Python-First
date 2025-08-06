# Handling error instead of letting it crash 
try:
    num=int(input("Enter a number"))
    result=10/num
    print("The result is ",result)

except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("This is not valid! It's a number.")
# 10.Write a program that asks the user to enter a number. Use try and except to handle both ZeroDivisionError and ValueError.
try:
    num =int(input("Enter a number:"))
    result = 10/ num
    print("The result is:", result)

except ZeroDivisionError:
    print("Don't try divide by zero.")

except ValueError:
    print("That's not a valid number.")
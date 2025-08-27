# 9. What is exception handling? Explain with an example where the user tries to divide by zero.

try:
    num =int(input("Enter a number:"))
    result = 20/ num
    print("The result is:", result)

except ZeroDivisionError:
    print("Don't divide by Zero.")

# Finally key in Exception handling

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)

except:
    print("Erro: Denominator cannot be 0.")

finally: print("This is finally block.")
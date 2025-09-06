# 
def cake_calculator(flour, sugar):
    cakesFromFlour = flour // 100
    cakesFromSugar = sugar // 50

    cakes = min(cakesFromFlour, cakesFromSugar)

    remainingFlour = flour - (cakes * 100)
    remainingSugar = sugar - (cakes * 50)

    return [cakes, remainingFlour, remainingSugar]

# print(cake_calculator(350, 200))
# print(cake_calculator(120, 45))

print(f"The total baked cake with remaining flour and sugar respectively is ",cake_calculator(350, 200))
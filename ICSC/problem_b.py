# -----Cake Calculator-----
def cake_calculator(flour, sugar):

    # Recipe requirements per cake
    flourPerCake = 100
    sugarPerCake = 50

    # Let's calcuate the maximun cakes based on each ingredient
    maxCakesFromFlour = flour // flourPerCake
    maxCakesFromSugar = sugar // sugarPerCake

    # Let's limit ingredient determines how many cakes we can make
    cakesPossible = min(maxCakesFromFlour, maxCakesFromSugar)

    # Let's calculate leftover indredients
    remainingFlour = flour - (cakesPossible * flourPerCake)
    remainingSugar = sugar - (cakesPossible * sugarPerCake)

    return [cakesPossible, remainingFlour, remainingSugar]

# print(cake_calculator(350, 200))
# print(cake_calculator(120, 45))

print(f"The total baked cakes and remaining flour , sugar respectively is ",cake_calculator(350, 200))
# ------Long (Normal) Way
# squares=[]
# for x in range(5):
#     squares.append(x*x)
#     print(squares)

# -------Short (Comprehension) Way
# squares=[x*x for x in range(5)]
# print(squares)

# -------Double the numbers
# nums=[1,3,4,9]
# doubled=[x*2 for x in nums]
# print(doubled)

# -------UpperCase letter
letters=['a', 'b', 'c']
upperLetters=[ch.upper() for ch in letters]
print(upperLetters)

# ---------Get only even numbers
value=[1,4,5,2,3,7,8,6]
onlyEven=[x for x in value if x%2==0]
print(onlyEven)

# --------Get only odd numbers
value=[1,3,4,5,6,7,8]
# onlyOdd=[x for x in value if x%2!=0]
onlyOdd=[x for x in value if x%2==1]
print(onlyOdd)
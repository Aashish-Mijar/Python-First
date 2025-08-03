text="Programming"
text2="Aashish"

# ---- Slicing from 0 to 5 index
print(text[0:6])

# ---- Slicing from idx 2 to end
print(text[2:])

# ----- Whole string
print(text[:])

# ------ slice every 2nd character
print(text[::2])

# ------ Slice every 2nd character from idx 1
print(text[1::2])

# ------ String reversed
print(text[::-1])

# ----- Start at idx 5, go backward to idx 3 (stop before 2)
print(text2[5:2:-1])
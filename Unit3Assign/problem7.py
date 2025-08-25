
# 7. What is a dictionary in Python? Write a program to count the frequency of each letter in a given string using a dictionary.

letter = "Rewrite".lower()  # .lower() for converting letter uppercase and lowercase
frequency_letter = {}  #empty dictionary

for text in letter:
    if text in frequency_letter:
        frequency_letter[text] +=1 
    else:
        frequency_letter[text] =1


for char, frequency in frequency_letter.items():
    print(f"The '{char}' repeat in '{frequency}' times. ")


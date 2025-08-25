# Given a string "ProgrammingInPython", write Python statements to:
"""    • Slice out “Programming”
       • Reverse the whole string
       • Check if "Python" is in the string """

text = "ProgrammingInPython"

print("This is the original text:",text)
   # slice out "Programming" from the word
print("Slice the word from text:",text[0:11])
    
    # reverse the whole string 
print("Reverse whole string of text:", text[::-1])

    # check "Python" is string 
print("Python is in the string?", "Python" in text)



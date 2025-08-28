# Write program to create dictionary, add elements in dictionary, remove elements from dictionary and display dictionary items. 

# create dictionary
dictionary = {
    'name': 'Dipisha',
    'age': 12,
    'city': 'Munich'
}

print("The original dictionary: " , dictionary)

# adding elements
dictionary['country'] = 'Germany'
dictionary['hobby'] = 'Coding'
print("After adding elements: " , dictionary)

# removing elements
del dictionary['age']      # removing age by using "del" keyword
print("After removing elements: " , dictionary)

remove_data = dictionary.pop('hobby') # removing hobby by using "pop" keyword
print("After removing 'hobby': " , dictionary)

# display items
for key, value in dictionary.items():
    print(key, ":", value)

    # print(f"{key} : {value}")
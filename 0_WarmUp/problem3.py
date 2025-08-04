import os
# Select the directory whose content you want to list
directory_path = '/Files_Semesters'

# Use the os module to list the directory content
contents=os.listdir(directory_path)
print("Contents of the directory :", directory_path)
for item in contents:
    print(item)
# 6. Write a Python program to:
    # • Create a dictionary with student names and their grades
    # • Retrieve a grade
    # • Add a new student
    # • Remove an existing student


# creating student details
student_details = { 
    "Dipisha": "A++",
    "Dikshya": "A",
    "Darshan": "B++"
}

# reteriving student grade
print("The grade of Dipisha: ", student_details["Dipisha"])


# add new student 
student_details["Levent"] = "B" 
print("New student add:", student_details)

# remove student
del student_details["Dikshya"]
print("Remove Dikshya student from student_details:",student_details)
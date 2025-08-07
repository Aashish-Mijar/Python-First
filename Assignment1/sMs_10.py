# --- Mutable
student_names=["Aashish", "Bibsh", "Caroline"]

# --- Immutable
student_ids=(101, 102, 103)

student_courses={
    101:["Maths", "Computer"],
    102:["Science", "Maths"],
    103:["Finance", "Maths"],
}

unique_subjects={"Maths", "Computer", "Science", "Finance"}

# ----- Operations
student_names.append("Meera")
new_id=104
student_ids+=(new_id,)
student_courses[new_id]=["English", "Marketing"]
unique_subjects.update(["English", "Marketing"])

# student_courses.remove("Caroline")

# student_ids[101].append("AI")

print("Student Names: ", student_names)
print("Students Ids: ", student_ids)
print("Student-Courses Mapping: ", student_courses)
print("Unique Subjects: ", unique_subjects)
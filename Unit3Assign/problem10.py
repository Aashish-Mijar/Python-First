# Imagine you’re creating a student management system. Identify which data structure (list, tuple, dictionary, or set) would be best for storing:
"""    • Student names 
       • Immutable student ID   
       • Student-course mapping  
       • List of unique subjects   """
#Explain why each structure is suitable. 

# using list for collect student names 
student_names = ["Gaurav", "Kartik", "karan", "Samrat"]

# using tuple for immutable student ID
student_Id = (1, 2, 3, 4)

# using dictionary for mapping student-course
student_course = {
   "1" : ["Digital Logic", "Python"], 
   "2": ["Computer Science", "Python"],
   "3": ["C", "Python"],
   "4": ["Math", "Python"]
}

  # using set for unique subjects
subjects = { "Digital Logic", "Python", "Computer Science", "C", "Math"}

 # create a new variable for convert set into list 
subject_list = list(subjects)

print(f" Id: {student_Id[1]}, Name:{student_names[1]}, Courses:{student_course["1"]},Subject: {subject_list[1]}")
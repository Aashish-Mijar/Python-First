students={
    "Aashish":{"lname":"Mijar", "grade":'A'},
    "Meera":{"lname":"S.K", "grade":'A'}
}
# print(students["Meera"]["grade"])

students["Deepsha"]={"lname":"Dumre", "grade":'A'}
students["Prabin"]={"lname":"Kunwar", "grade":'A'}

del students["Aashish"]
print(students)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

Student_grade={}

for student,score in student_scores.items():
    if score>=91 and score<=100:
        print("excelent")
    elif score>=81 and score<=90:
        print("exceptation")
    elif score>=70 and score<=80:
        print("Good")
    else:
        print("fail")

    Student_grade[student]=score

print(Student_grade)

student = {}
student["Name"] = "Seth Ramsey"
student["Age"] = 22
student["Major"] = ['Supply Chain Management','Management Information Systems']
student["Hobbies"] = ["reading", "disc golf", "video games"]

student['State'] = 'Texas'

student['Age'] += 1

for i in student:
    print(f'{i} - {student[i]}')
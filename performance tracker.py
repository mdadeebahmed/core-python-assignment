def averageMarks(students_data):
    results = {}
    for student, marks in students_data.items():
        avg = round(sum(marks) / len(marks), 2)
        results[student] = avg

    return results

def topPerformer(students_data):
    averages = averageMarks(students_data)
    top_student = max(averages, key=averages.get)
    return f'Top Performer: "{top_student}"'

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
print(averageMarks(students))
print(topPerformer(students))
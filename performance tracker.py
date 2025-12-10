def studentPerformance(students_data):
    results = {}
    for student, marks in students_data.items():
        avg = round(sum(marks) / len(marks), 2)
        results[student] = avg

    # Find top performer
    top_student = max(results, key=results.get)

    return results, f'Top Performer: "{top_student}"'

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
print(studentPerformance(students))
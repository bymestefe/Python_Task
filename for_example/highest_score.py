
	
# Let's find the highest exam grade, without using the max method
# En yüksek sınav notunu bulalım, max metodunu kullanmadan bulmaya çalışalım

number_of_student = int(input("enter the number of students = "))

exam_grades = []

for result in range(number_of_student):
    exam_grade = int(input("enter exam grade = "))
    exam_grades.append(exam_grade)

# print(exam_results)

highest_grade = exam_grades[0]

for i in exam_grades:
    if i > exam_grades[0]:
        highest_grade = i

print(f"Highest Grade : {highest_grade}")
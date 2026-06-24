def calculate_salary(name, basic, bonus):
    total = basic + bonus
    return name, total


employees = []
salary_list = []

for i in range(3):
    name = input("Enter Name: ")
    basic = int(input("Enter Basic Salary: "))
    bonus = int(input("Enter Bonus: "))

    emp_name, total_salary = calculate_salary(name, basic, bonus)

    employees.append(emp_name)
    salary_list.append(total_salary)

    print(emp_name, "Total Salary:", total_salary)

print("Total Employees:", len(employees))
print("All Salaries:", salary_list)

def calc_students (name,class_name,grade):
    total = class_name+grade
    return name, total

students = []
grade_list = []

for i in range(3):
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    grade = (input("Enter Grade: "))

    student_name, student_class = calc_students(name,class_name,grade)
    students.append(student_name)
    grade_list.append(student_class)


    print(student_name , "Total Grade:", grade)

print("Total Students:", len(students))
print("Total Grades:", grade_list)


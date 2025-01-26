'''
Author: Sourav V S
Date: 19-11-2024
This program is to find the employee with highest salary and total annual payroll expenses for all employees.
'''
emp_info = [("Ethan","Ethical Hacker",60000.0),
            ("Zayn","Data Scientist",50000.0),
            ("Neo","Web Developer",45000.0),
            ("John Wick","Robotics",49000.0)]
total_annual_expenses = 0
threshold = float(input("Enter the threshold salary: "))
for employee in emp_info:
    name,department,salary = employee
    total_annual_expenses += salary * 12
    if salary > threshold:
        print (f"Employees with monthly salary above threshold: {name}")
print(f"Total annual payroll expenses for all employees by the company: {total_annual_expenses}")

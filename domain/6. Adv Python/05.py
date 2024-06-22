emp_salary = [12, 13, 14]
emp_list = []
incremented_salary = [temp + (temp * 10 / 100) for temp in emp_salary]

emp_list.append(incremented_salary)

print(emp_list)

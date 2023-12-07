def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission_rate = 0.03
    elif 500 < sales <= 1000:
        commission_rate = 0.05
    else:
        commission_rate = 0.08

    commission = sales * commission_rate
    total_salary = base_salary + commission
    return total_salary


sales_manager1 = float(input("Please enter sales price to first manager: $"))
sales_manager2 = float(input("Please enter sales price to second manager: $"))
sales_manager3 = float(input("Please enter sales price to third manager: $"))

salary_manager1 = calculate_salary(sales_manager1)
salary_manager2 = calculate_salary(sales_manager2)
salary_manager3 = calculate_salary(sales_manager3)

print(f"\nSalary of the manager 1: ${salary_manager1}")
print(f"Salary of the manager 2: ${salary_manager2}")
print(f"Salary of the manager 3: ${salary_manager3}")

best_manager_salary = max(salary_manager1, salary_manager2, salary_manager3)
best_manager_index = [salary_manager1, salary_manager2, salary_manager3].index(best_manager_salary) + 1

print(f"\nThe best manager - manager {best_manager_index}")

bonus = 200
best_manager_salary_with_bonus = best_manager_salary + bonus
print(f"Salary of the best Employee: ${best_manager_salary_with_bonus}")

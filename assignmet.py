class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if target_name.lower() in emp.name.lower()]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []
        return result

    def print_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary (PM)")
            for emp in results:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    employee_table = EmployeeTable(employees)

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (> < <= >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the age to search for: "))
        results = employee_table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search for: ")
        results = employee_table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (> < <= >=): ")
        target_salary = int(input("Enter the salary to search for: "))
        results = employee_table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice.")
        return

    employee_table.print_results(results)

if __name__ == "__main__":
    main()

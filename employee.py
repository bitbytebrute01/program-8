def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee name : {name}\n"
        f"Employee ID   : {emp_id}\n"
        f"Department    : {department}\n"
        f"Salary        : {salary}"
    )
    return result


if __name__ == "__main__":
    name = "Aditya"
    emp_id = "01FE24BCA017"
    department = "BCA"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))
from employee import employee_details

def test_employee_output():
    expected_output = (
        "Employee name : Anusha\n"
        "Employee ID   : 01FE24BCA016\n"
        "Department    : BCA\n"
        "Salary        : 55000"
    )

    assert employee_details("Anusha", "01FE24BCA016", "BCA", 55000) == expected_output
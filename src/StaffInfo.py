class StaffInfo:
    """
    Author: Zhiming Liu
    """
    empid = ""
    gender = ""
    age = 0
    sales = 0
    bmi = ""
    salary = ""
    birthday = ""

    def __init__(self, new_empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        self.empid = new_empid
        self.gender = new_gender
        self.age = new_age
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday

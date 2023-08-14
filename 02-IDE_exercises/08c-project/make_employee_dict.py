class Employee:
    def __init__(self, name: str, ID_number: str, salary: int, email_address: str):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address
    
    def get_name(self):
        return self.name
    
    def get_ID_number(self):
        return self.ID_number
    
    def get_salary(self):
        return self.salary
    
    def get_email_address(self):
        return self.email_address

def make_employee_dict(names: list[str], IDs: list[str], salaries: list[int], emails: list[str]) -> dict:
    index = 0
    new_dict = {}
    for employee in range(len(names)-1):
        employee = Employee(employee, IDs[index], salaries[index], emails[index])
        new_dict[IDs[index]] = [names[index], salaries[index], emails[index]]
        index +=1
    return new_dict


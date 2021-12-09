from person_company import person_company


class employee(person_company):
    def __init__(self, company_name, department_name, name, age, gender, group):
        super().__init__(company_name, department_name, name, age, gender)
        self.group = group

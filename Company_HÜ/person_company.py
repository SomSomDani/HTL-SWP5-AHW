from department import department


class person_company(department):
    def __init__(self, company_name, department_name, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        super().__init__(company_name,department_name)

from company import company


class department(company):
    def __init__(self, company_name, department_name):
        super().__init__(company_name)
        self.department_name = department_name

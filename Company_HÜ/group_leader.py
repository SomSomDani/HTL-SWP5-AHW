from employee import employee


class group_leader(employee):
    def __init__(self,  company_name, department_name, name, age, gender, group, group_leader_id):
        super().__init__(company_name, department_name, name, age, gender, group)
        self.group_leader_id = group_leader_id

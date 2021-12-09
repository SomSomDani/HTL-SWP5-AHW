from company import company
from department import department
from employee import employee
from group_leader import group_leader
from person_company import person_company


def create_company(comp_name):
    comp = company(comp_name)
    return comp


def create_department(comp_name, dep_name):
    dep = department(comp_name, dep_name)
    return dep


def adding_departments(user_c, user_d):
    e = create_department(user_c, user_d)
    departments.append(e.department_name)


def number_departments(d):
    n = len(d)
    print("Anzahl der Abteilungen: " + str(n))
    return d


def create_person(comp_name, dep_name, name, age, gender):
    per = person_company(comp_name, dep_name, name, age, gender)
    return per


def adding_person(c, d, n, a, g):
    p = create_person(c, d, n, a, g)
    people.append(p.gender)


def number_gender(p):
    n = len(p)
    f = 0
    m = 0
    for i in range(n):
        g = p[i]
        if g == "m":
            m += 1
        else:
            f += 1
    print("Anteil Männer im Unternehmen: " + str((m / n) * 100) + " %")
    print("Anteil Frauen im Unternehmen: " + str((f / n) * 100) + " %")
    print("Anteil Frauen zu Männern im Unternehmen: " + str(m != 0 if f/m else 0))


def create_employee(c, d, n, a, g, gr):
    empl = employee(c, d, n, a, g, gr)
    return empl


def adding_employee(c, d, n, a, g, gr):
    e = create_employee(c, d, n, a, g, gr)
    people.append(e.gender)
    employees.append(e.department_name)


def create_group_leader(c, d, n, a, g, gr, gn):
    gl = group_leader(c, d, n, a, g, gr, gn)
    return gl


def adding_group_leader(c, d, n, a, g, gr, gn):
    gl = create_group_leader(c, d, n, a, g, gr, gn)
    people.append(gl.gender)
    employees.append(gl.department_name)
    group_leaders.append(gl.group_leader_id)


def number_employees(e):
    n = len(e)
    print("Anzahl der Mitarbeiter in der Firma: " + str(n))


def number_group_leader(g):
    n = len(g)
    print("Anzahl der Gruppenleiter in der Firma: " + str(n))


def department_employees(emp,de):
    temp_map = {}
    for d in number_departments(de):
        temp_map[d] = 0
    for e in emp:
        for d in de:
            if d == e:
                temp_map[d] = temp_map[e] + 1
                break
    print(temp_map)


if __name__ == '__main__':
    departments = []
    people = []
    employees = []
    group_leaders = []
    user_c = input("Name of the company: ")
    cc = create_company(user_c)
    dep = False
    while dep == False:
        user_r = input("\nAdding an department [r] or [s]: ")
        if user_r.lower() == "r":
            user_d = input("Name of the department: ")
            adding_departments(user_c, user_d)
        if user_r.lower() == "s":
            dep = True
    pers = False
    while pers == False:
        user_r = input("\nAdding an person [p] or [s]: ")
        if user_r.lower() == "p":
            user_d = input("Name of the department the person works in: ")
            user_n = input("Name of the person: ")
            user_a = int(input("Age of the person: "))
            user_g = input("Gender of the person: ")
            adding_person(user_c, user_d, user_n, user_a, user_g)
        if user_r.lower() == "s":
            pers = True
    emp = False
    while emp == False:
        user_r = input("\nAdding an employee [e] or [s]: ")
        if user_r.lower() == "e":
            user_d = input("Name of the department the employee works in: ")
            user_n = input("Name of the employee: ")
            user_a = int(input("Age of the employee: "))
            user_g = input("Gender of the employee: ")
            user_gr = int(input("Group the employee is: "))
            adding_employee(user_c, user_d, user_n, user_a, user_g, user_gr)
        if user_r.lower() == "s":
            emp = True
    gl = False
    while gl == False:
        user_r = input("\nAdding an group leader [g] or [s]: ")
        if user_r.lower() == "g":
            user_d = input("Name of the department the group leader works in: ")
            user_n = input("Name of the group leader: ")
            user_a = int(input("Age of the group leader: "))
            user_g = input("Gender of the group leader: ")
            user_gr = int(input("Group the group leader leads: "))
            user_gn = int(input("Group leader id is: "))
            adding_group_leader(user_c, user_d, user_n, user_a, user_g, user_gr, user_gn)
        if user_r.lower() == "s":
            gl = True
    # 1
    number_employees(employees)
    number_group_leader(group_leaders)
    # 2
    number_departments(departments)  # Anzahl der Abteilungen
    # 3
    department_employees(employees, departments)
    # 4
    number_gender(people)  # Anzahl der Männer und Frauen und Verhältnis im Gesamten


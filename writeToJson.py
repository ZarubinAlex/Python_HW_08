
# Для создания и заполнения пустых файлов, разкоментировать:

# import json
# import fixtables as glob
# import temptables as temp


# positions_json = json.dumps(glob.positions)
# departments_json = json.dumps(glob.departments)
# employees_json = json.dumps(temp.employees)
# address_json = json.dumps(temp.address)
# email_json = json.dumps(temp.email)
# tel_json = json.dumps(temp.phones)

# with open("HW_08_sprav\\positions.json", "w") as file:
#     file.write(positions_json)
# with open("HW_08_sprav\\departments.json", "w") as file:
#     file.write(departments_json)

def addEmployees(json):
    with open("HW_08_sprav\\employees.json", "w") as file:
        file.write(json)

def addAddress(json):
    with open("HW_08_sprav\\address.json", "w") as file:
        file.write(json)

def addEmail(json):
    with open("HW_08_sprav\\email.json", "w") as file:
        file.write(json)

def addPhone(json):
    with open("HW_08_sprav\\phones.json", "w") as file:
        file.write(json)


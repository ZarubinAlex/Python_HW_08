
import writeToJson as wr
import json

def lastID(fileName):

    with open(fileName, "r") as file:
        jsonText = file.read()
    text = json.loads(jsonText)

    for i in text: next
    return int(i['ID'])

def printFileEmpl(fileName):

    with open(fileName, "r") as file:
        jsonText = file.read()
    text = json.loads(jsonText)

    for i in text: 
        print(f'{i["ID"]}. {i["Фамилия"]} {i["Имя"]} {i["Отчество"]}, {i["Дата рождения"]}')

def printFilePosDep(fileName):

    with open(fileName, "r") as file:
        jsonText = file.read()
    text = json.loads(jsonText)

    print('')
    for i in text: 
        print(f'{i["ID"]}. {i["Название"]}')


def addEmployees():

    fileName = "HW_08_sprav\\departments.json"
    count = lastID(fileName)
    printFilePosDep(fileName)

    while True:
        departments = input('В какой отдел (номер): ')
        if departments.isdigit(): 
            departments = int(departments)
            if 1 <= departments <= count:
                break

    fileName = "HW_08_sprav\\positions.json"
    count = lastID(fileName)
    printFilePosDep(fileName)

    while True:
        positions = input('На какую должность (номер): ')
        if positions.isdigit(): 
            positions = int(positions)
            if 1 <= positions <= count:
                break

    lastName = input('Фамилия: ')
    firstName = input('Имя: ')
    secondName = input('Отчество: ')
    birthday = input('Дата рождения: ')

    fileName = "HW_08_sprav\\employees.json"
    n = lastID(fileName) + 1

    with open(fileName, "r") as file:
        jsonEmpl = file.read()
    emploeyss = json.loads(jsonEmpl)

    emploeyss.append({
        'ID': str(n), 
        'Фамилия' : lastName, 
        'Имя' : firstName,
        'Отчество' : secondName,
        'Дата рождения' : birthday,
        'ID Должности' : str(positions), 
        'ID Отдела' : str(departments)
        })

    wr.addEmployees(json.dumps(emploeyss))
    print('')
    print(f'Добавлен новый сотрудник № {n}')
    printFileEmpl(fileName)



def addAddress():

    print('')
    print('Выберите сотрудника, которому добавить адрес:')
    fileName = "HW_08_sprav\\employees.json"
    printFileEmpl(fileName)

    n = input('Номер сотрудника: ')
    city = input('Город : ')
    street = input('Улица: ')
    house = input('Дом: ')
    apartment = input('Квартира: ')

    fileName = "HW_08_sprav\\address.json"
    with open(fileName, "r") as file:
        jsonAddress = file.read()
    address = json.loads(jsonAddress)

    address.append({
        'ID': n,
        'Город' : city,
        'Улица' : street,
        'Дом' : house,
        'Квартира' : apartment})
    wr.addAddress(json.dumps(address))
    print(f'Адрес добавлен сотруднику {n}')



def addPhone():

    print('')
    print('Выберите сотрудника, которому добавить телефон:')
    fileName = "HW_08_sprav\\employees.json"
    printFileEmpl(fileName)

    n = input('Номер сотрудника: ')
    phone = input('Телефон: ')

    fileName = "HW_08_sprav\\phones.json"
    with open(fileName, "r") as file:
        jsonPhones = file.read()
    phones = json.loads(jsonPhones)

    phones.append({
        'ID': n,
        'Tel' : phone
        })
#    print(phones)
    wr.addPhone(json.dumps(phones))
    print(f'Телефонный номер добавлен сотруднику {n}')




def addEmail():    

    print('')
    print('Выберите сотрудника, которому добавить E-mail:')
    fileName = "HW_08_sprav\\employees.json"
    printFileEmpl(fileName)

    n = input('Номер сотрудника: ')
    email = input('E-mail: ')

    fileName = "HW_08_sprav\\email.json"
    with open(fileName, "r") as file:
        jsonPhones = file.read()
    emails = json.loads(jsonPhones)

    emails.append({
        'ID': n,
        'Email' : email
        })
    wr.addEmail(json.dumps(emails))
    print(f'E-mail добавлен сотруднику {n}')


def printAll():

    fileName = "HW_08_sprav\\employees.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    empl = json.loads(jsonText)

    fileName = "HW_08_sprav\\address.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    addr = json.loads(jsonText)

    fileName = "HW_08_sprav\\email.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    mail = json.loads(jsonText)

    fileName = "HW_08_sprav\\phones.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    phone = json.loads(jsonText)

    fileName = "HW_08_sprav\\departments.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    dep = json.loads(jsonText)

    fileName = "HW_08_sprav\\positions.json"
    with open(fileName, "r") as file:
        jsonText = file.read()
    pos = json.loads(jsonText)

    print('')
    for i in empl: 
        print(f'{i["ID"]}. {i["Фамилия"]} {i["Имя"]} {i["Отчество"]}, {i["Дата рождения"]}', end = ', ')
        for j in dep: 
             if j["ID"] == i["ID Отдела"]: print(f'отдел: {j["Название"]}', end = ', ')
        for j in pos: 
             if j["ID"] == i["ID Должности"]: print(f'должность: {j["Название"]}, оклад: {j["Оклад"]} руб.', end = '')
        print('\n\tE-mail: ', end = '')
        for j in mail: 
             if j["ID"] == i["ID"]: print(f'{j["Email"]}', end = ', ')
        print('\n\tТел: ', end = '')
        for j in phone: 
             if j["ID"] == i["ID"]: print(f'\t{j["Tel"]}', end = ', ')
        print('\n\tАдрес: ', end = '')
        for j in addr: 
             if j["ID"] == i["ID"]: print(f'\t{j["Город"]}, {j["Улица"]} {j["Дом"]}, {j["Квартира"]}')

        print('')


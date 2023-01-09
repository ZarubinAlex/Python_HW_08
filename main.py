import contacts

print('')
print('\
        1: Вывод всей информации о сотрудниках\n\
        2: Добавить Сотрудника\n\
        3: Добавить Адрес сотруднику\n\
        4: Добавить Телефон сотруднику\n\
        5: Добавить E-mail сотруднику')

while True:
    n = input('Выберите действие: ')
    if n.isdigit(): n = int(n)
    if   n == 1:
        contacts.printAll()
        break
    elif n == 2:
        contacts.addEmployees()
        break
    elif n == 3:
        contacts.addAddress()
        break
    elif n == 4:
        contacts.addPhone()
        break
    elif n == 5:
        contacts.addEmail()
        break

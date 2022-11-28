from Stud_csv import file_open, insert, show_rows

FILENAME = "Data.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по ФИО',
    '5': 'Найти по группе',
    '6': 'Вывести старше 18',
    '7': 'Сохранить в файл',
    '8': 'Вывести записи',
    '0': '<-Меню',
    'exit': 'Выход'
}
for k,v in MENU.items():
    print(k, '-', v)

while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == '2':
        insert(input('фио: '), input('пол: '), input('возраст: '), input('телефон: '),
               input('почта: '), input('группа: '), input('курс: '))

    elif action == '8':
        show_rows()

    elif action == 'exit':
        break
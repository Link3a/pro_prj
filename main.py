from Stud_csv import file_open

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
    elif action == 'exit':
        break
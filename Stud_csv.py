import csv

csv_file = []

# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))

# Добавление
def insert(num, fio, gen, age, tel, mail, group, cours):
    try:
        mx = max(csv_file, key=lambda x: int(x['ном']))
        csv_file.append({'ном': int(mx['ном'])+1,
                        'фио': fio,
                         'пол': gen,
                         'возраст': age,
                         'телефон': tel,
                         'почта': mail,
                         'группа': group,
                         'курс': cours})
    except Exception as e:
        return f"Ошибка при добавлении новой записи {e}"
    print("Данные добавлены")

# Удаление
def drop_by_arg(val, col_name="фио"):
    global csv_file
    try:
        cvs_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f"Строка со значением {val} поля {col_name} не найдена"
        return f"Строка со значением {val} поля {col_name} удалена!"
# Поиск по фио
def find(val, col_name='фио'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))
# Поиск по группе
def find(val, col_name='группа'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))
# Старше 18
def find(val, col_name='возраст'):
    print(*list(filter(lambda x: x[col_name] >= val, csv_file)))
# Функция Сохранить
def save(fine_name):
   with open(fine_name, 'w', encoding='utf-8', newline='') as file:
        columns = ['ном', 'фио', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные сохранены")


# Вывод списка записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<25}{:<10}{:<8}{:<12}{:<25}{:<8}{:<8}'.format('ном', 'фио', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс'))
        for el in csv_file:
            print('{:<5}{:<25}{:<10}{:<8}{:<12}{:<25}{:<8}{:<8}'.format(el['ном'], el['фио'], el['пол'],
                                                                        el['возраст'], el['телефон'], el['почта'], el['группа'], el['курс']))


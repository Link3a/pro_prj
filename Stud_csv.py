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


# Вывод списка записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<25}{:<10}{:<8}{:<12}{:<25}{:<8}{:<8}'.format('ном', 'фио', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс'))
        for el in csv_file:
            print('{:<5}{:<25}{:<10}{:<8}{:<12}{:<25}{:<8}{:<8}'.format(el['ном'], el['фио'], el['пол'],
                                                                        el['возраст'], el['телефон'], el['почта'], el['группа'], el['курс']))


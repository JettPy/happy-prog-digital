def get_menu_item() -> int:
    # Функция вывода меню и выбора пункта
    while True:
        try:
            print("Выберите пункт меню:\n")
            print("1. Создать новою запись")
            print("2. Просмотреть таблицу")
            print("3. Найти все похожие записи")
            print("4. Отсортировать таблицу")
            print("5. Выход\n")
            n = int(input("> "))
            break
        except ValueError:
            print("Попробуйте еще раз\n")
    return n


def append_new_record() -> list:
    # Добавление новой записи
    while True:
        try:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            day, month, year = map(int, input('Введите дату рождения (dd): ').split())
            break
        except ValueError:
            print('Не корректные данные, попробуйте еще раз\n')
    new_record = [name, surname, day, month, year]
    return new_record


def view_table(records: list[list[str, str, int, int, int]]) -> None:
    # Вывод таблицы в консоль
    print("+------------------------------------------------------+")
    print("|      Имя      |    Фамилия    | День | Месяц |  Год  |")
    print("+------------------------------------------------------+")
    for record in records:
        print("| %13s | %13s |   %02d |   %02d  |  %04d |" % (record[0], record[1], record[2], record[3], record[4]))
    print("+------------------------------------------------------+\n")


def find_common_records(records: list[list[str, str, int, int, int]]):
    # Поиск всех подходящих записей
    search_str = input('Что ищем?\n> ')
    is_first = True
    for record in records:
        line_to_str = [str(x) for x in record]
        line = ' '.join(line_to_str)
        if line.find(search_str) != -1:
            if is_first:
                print("+------------------------------------------------------+")
                print("|      Имя      |    Фамилия    | День | Месяц |  Год  |")
                print("+------------------------------------------------------+")
                is_first = False
            print("| %13s | %13s |   %02d |   %02d  |  %04d |" % (record[0], record[1], record[2], record[3], record[4]))
    if not is_first:
        print("+------------------------------------------------------+\n")
    else:
        print('Ничего не найдено\n')


def comparator(n: int):
    # Компаратор для сортировки
    return lambda x: x[n - 1]


def sort_records(records: list[list[str, str, int, int, int]]) -> list[list[str, str, int, int, int]]:
    # Сортировка записей по заданному параметру
    n = 0
    while True:
        try:
            print("Выберите параметр для сортировки")
            print("1. Имя")
            print("2. Фамилия")
            print("3. Год")
            print("4. Месяц")
            print("5. День")
            n = int(input('> '))
            break
        except ValueError:
            print("Попробуйте еще раз\n")
    cmp = comparator(n)
    return sorted(records, key=cmp)


# Основная программа
database = []
try:
    file = open('notebook.txt', encoding='utf-8')
    for line in file:
        name, surname, year, month, day = line.split()
        year = int(year)
        month = int(month)
        day = int(day)
        database.append([name, surname, year, month, day])
    file.close()
except FileNotFoundError:
    pass
try:
    while True:
        item = get_menu_item()
        if item == 1:
            new_entry = append_new_record()
            database.append(new_entry)
        elif item == 2:
            view_table(database)
        elif item == 3:
            find_common_records(database)
        elif item == 4:
            database = sort_records(database)
        elif item == 5:
            break
        else:
            print("Нет такого варианта")
finally:
    file = open('notebook.txt', 'w', encoding="utf-8")
    for line in database:
        line_to_str = [str(x) for x in line]
        file.write(' '.join(line_to_str)+'\n')
    file.close()


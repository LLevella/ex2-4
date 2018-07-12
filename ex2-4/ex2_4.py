
# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

# Генерировать абсолютный путь до папки с миграциями. Скрипт при этом лежит в одной папке с папкой 'Migrations', 
# но запускать мы его можем из любой директории - он будет работать корректно.

import myfunclib

if __name__ == '__main__':
   
    ps = myfunclib.get_params()
    migration_directory, *extensions = ps
    fn = []
    while True:
        sparam = ""
        com = input("Введите команду: q - выход, ns - новый поиск, ds - уточняющий поиск\n")

        if com.lower() == "q":
            break

        if com.lower() == "ns" or com.lower() == "ds":
            sparam = input("Введите искомую строку:\n")

        if not sparam:
            print("Пустой или неверный параметр")
        else:
            if com.lower() == "ns":
               fn = myfunclib.get_files_by_extensions(migration_directory, myfunclib.search_files_in_directory(migration_directory), extensions)

            if not fn:
                print("Список файлов пуст")
                break

            fn = myfunclib.get_files_by_words(sparam, fn)
            print("Найдено {} файлов:".format(len(fn)))
            print("\n".join(fn))
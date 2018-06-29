
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

import os
import sys

def get_params():
    migrations = 'Migrations'
    file_extension = "sql"
    ps = []
    lcs = len(sys.argv)
    if lcs > 1:
        for i in range(1,lcs):
            ps.append(sys.argv[i])
        if lcs < 3:
             ps.append(file_extension)
    else:
        ps.append(migrations)
        ps.append(file_extension)
    return ps



def create_abs_dir_name(dir_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    migr_dir = os.path.join(current_dir,dir_name)
    if not os.path.lexists(migr_dir):
        return None
    return migr_dir

def search_files_in_directory(dir_name):
    files_names = []
    migr_dir = create_abs_dir_name(dir_name)
    if migr_dir is not None:
        files_names = os.listdir(migr_dir)
    return files_names


def get_files_by_extensions(dir_name, files_names, file_extension):
    f_by_ext = []
    migr_dir = create_abs_dir_name(dir_name)
    if migr_dir is not None:
        for fn in files_names:
            s_ext = fn.split(".")[-1]
            if file_extension.count(s_ext.lower())>0:
                f_by_ext.append(os.path.join(migr_dir, fn))
    return f_by_ext

def get_files_by_words(sparam, l_files):
    new_l_files=[]
    for l_file in l_files:
        with open(l_file, 'r') as fin:
            text = fin.read()
            n = text.find(sparam)
            if n!=-1:
                new_l_files.append(l_file)

    return new_l_files

if __name__ == '__main__':
   
    ps = get_params()

    fn = []
    while True:
        sparam = ""
        com = input("Введите команду: q - выход, ns - новый поиск, ds - уточняющий поиск\n")

        if com.lower() == "q":
            break

        if com.lower() == "ns" or com.lower() == "ds":
            sparam = input("Введите искомую строку:\n")

        if len(sparam) == 0:
            print("Пустой или неверный параметр")
        else:
            if com.lower() == "ns":
               fn = get_files_by_extensions(ps[0], search_files_in_directory(ps[0]), ps[1:])

            if len(fn) == 0:
                print("Список фалов пуст")
                break

            fn = get_files_by_words(sparam, fn)
            print("Найдено {} файлов:".format(len(fn)))
            #for fel in fn:
            #    print(fel)
            print("\n".join(fn))
    pass

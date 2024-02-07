# Подключаем встроенные библиотеки для работы с файловой системой
import os
import shutil


# Функция создания словаря по path
def foo(directory):
    # Создаем пустой список
    files = []  # для файлов всего каталога
    FilesNames = list()  # для файлов одного расширения

    # Инициализируем пустой словарь
    Dictionary = {}

    # Инициализируем переменную для расширений
    Current_extension = ""

    # Функция определения формата файла
    def sort_function(file):
        parts = file.split('.')
        extension = parts[-1]
        return extension

    # Добавляем файлы в список
    files += os.listdir(directory)

    # Сортируем файлы по расширениям
    files = sorted(files, key=sort_function)

    # Вывод отсортированного списка файлов
    print("Отсортированный список файлов в указанном каталоге:")
    print(files)
    print()  # Пропуск строки

    i = 0  # Переменная для счетчика в цикле
    # Выполнить цикл, пока не пройдемся по всем файлам
    while i < len(files):
        # Если файл находится на первом месте в списке
        if i == 0:
            # Записать расширение в переменную
            Current_extension = sort_function(files[i])
            # Добавить в список файл с данным расширением
            FilesNames.append(files[i])
        # Если файл не первый в списке
        else:
            # Записываем расширение текущего файла в новую переменную Next_extension
            Next_extension = sort_function(files[i])
            # Если предыдущее расширение равно расширению текущего файла,
            # то добавить файл в список с данным расширением
            if Current_extension == Next_extension:
                FilesNames.append(files[i])
            # Если предыдущее расширение отличается от расширения текущего файла, то
            else:
                # добавить в словарь пару ключ-значение
                Dictionary[Current_extension] = FilesNames
                # обнулить список файлов старого расширения
                FilesNames = list()
                # Поменять расширение на новое
                Current_extension = Next_extension
                # добавить в этот список файл с новым расширением
                FilesNames.append(files[i])
        # Если файл в общем списке файлов последний
        if i == (len(files) - 1):
            # добавить ключ-значение в словарь
            Dictionary[Current_extension] = FilesNames
            # обнулить список файлов предыдущего расширения
            FilesNames = list()
        # увеличиваем итерацию на 1
        i += 1
    # В качестве результата возвращаем словарь
    return Dictionary


# Основная функция main
def main():
    path = "../FolderWithFiles"     # Указываем директорию нужной папки
    result = foo(path)              # Вызываем функцию создания словаря
    print("Полученный словарь:")
    print(result)                   # Печатаем результат

    # Проходим по словарю и копируем файлы в другую папку
    i = 0
    for ext, listOfFiles in result.items():
        # Копируем каждый файл одного расширения
        while i < len(listOfFiles):
            shutil.copy2('../hdfs/{}'.format(listOfFiles[i]), '../airflow/{}'.format("new_" + listOfFiles[i]))
            i += 1
        i = 0

    # Второй способ - все файлы из одного каталога копируются в файлы другого каталога
    folder_from = r'../hdfs_ex'
    folder_to = r'../airflow_ex'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))


main()  # Вызываем основную функцию main

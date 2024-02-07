# Подключаем встроенную библиотеку для работы с файловой системой
import os


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


main()  # Вызываем основную функцию main

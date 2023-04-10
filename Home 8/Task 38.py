def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())


def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input())


def find_file():
    find_info = input()
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_file():
    find_info = input()
    with open(path_file, 'r+', encoding='UTF-8') as f:
        newfile = f.readlines()
    for i in range(len(newfile)):
        if find_info.casefold() in newfile[i].casefold():
            print(newfile[i])
            if input("Удалить(Да/Нет)") == "Да":
                newfile[i] = ""
            elif input("Изменить(Да/Нет)") == "Да":
                newfile = input("Введите Измененный вариант"+'\n')
    with open(path_file, 'w', encoding="UTF-8") as f:
        f.writelines(newfile)


def main():
    while True:
        ask = input("что выхотите сделать?(Чтение/Запись/Поиск/Изменение(Удалить)")
        if ask == "Чтение":
            write_file()
        elif ask == "Поиск":
            find_file()
        elif ask == "Запись":
            read_file()
        elif ask == "Изменение":
            change_file()
        else:
            break


path_file = r'Telephonebook.txt'
main()

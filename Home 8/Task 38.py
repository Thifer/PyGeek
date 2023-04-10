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
    new_info = input()
    with open(path_file, 'r+', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else:
                    continue


def main():
    cnt = True
    while cnt:
        ask = input("что выхотите сделать?(Чтение/Запись/Поиск/Изменение")
        if ask == "Чтение":
            write_file()
        elif ask == "Поиск":
            find_file()
        elif ask == "Запись":
            read_file()
        elif ask == "Изменение":
            change_file()
        ask = input("Вы закончили?(Да/Нет)")
        if ask == "Да":
            cnt = False


path_file = r'Telephonebook.txt'
main()

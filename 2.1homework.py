"""
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p - people - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

l - list - команда, которая выведет список всех документов в формате: passport "2207 876234" "Василий Гупкин";

s - shelf - команда, которая спросит номер документа и выведет номер полки, на которой он находится;

a - add - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, типа, имя владельца
    и номер полки, на котором он будет храниться;

-----------------------------------------------------------------------------------------------------------------------

d - delete - команда, которая спросит номер документа и удалит его из каталога и из перечня полок;

m - move - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;

as - add shelf - команда, которая спросит номер новой полки и добавит ее в перечень.

"""

# Каталог документов
documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },

    {
        "type": "invoice",
        "number": "11-2",
        "name": "Генрих Покемонов"
    },

    {
        "type": "insurance",
        "number": "10006",
        "name": "Аристарх Павлов"
    }
]

# Перечень полок
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

commands = ['p', 'l', 's', 'a', 'd', 'm', 'as']


def get_name_by_document(number: str) -> str:
    for document in documents:
        if document['number'] == number:
            return document['name']


def get_all_documents() -> list:
    document_list = list()
    for document in documents:
        document_list.append(f"{document['type']} '{document['number']}' '{document['name']}'")
    return document_list


def get_place_document(number: str) -> str:
    for shelf, document in directories.items():
        if number in document:
            return shelf


def add_new_document(doc_type: str, doc_number: str, doc_owner: str, shelf: str) -> str:
    for document in documents:
        if document['type'] == doc_type and document['number'] == doc_number and document['name'] == doc_owner:
            return "Такой документ уже есть в базе!"
        else:
            documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
            directories[shelf].append(document_number)
            return f"Документ добавлен в базу и будет храниться на полке {shelf}"


def del_document(doc_number: str) -> str:
    for document in documents:
        if document['number'] == doc_number:
            documents.remove(document)
            for document in directories.values():
                if doc_number in document:
                    document.remove(doc_number)
                    return f"Документ под номером {doc_number} из базы и с полки удален!"


def move_document(doc_number: str, shelf: str) -> str:
    for shelf_num, documents_number in directories.items():
        if doc_number in documents_number:
            if shelf_num == shelf:
                return "Документ уже находится в целевой папке!"
            else:
                documents_number.remove(doc_number)
                directories[shelf].append(doc_number)
                return f"Документ '{doc_number}' был перемещен на полку - '{shelf}'!"


def add_new_place(shelf: str) -> str:
    directories.update({shelf: []})
    return f"Полка под номером '{shelf}' успешно добавлена!"


if __name__ == '__main__':

    main_flag = True
    while main_flag:

        print("Программа Секретарь 2001")
        print("-" * 26)
        print("Перечень возможных команд:\n"
              "--------------------------\n"
              "p - узнать человека по номеру документа\n"
              "l - вывод всех документов в формате (документ номер_документа владелец)\n"
              "s - узнать местонахождение документа\n"
              "a - добавление нового документа в каталог и перечень полок\n"
              "d - удаление документа по номеру из каталога и перечня полок\n"
              "m - перемещение документа в целевую полку\n"
              "as - добавление новой полки\n")

        command = None
        global_flag = True
        while global_flag:
            command = str(input("Введите желаемую команду: "))
            if command not in commands:
                print("Неверная команда! Введите команду из перечня выше!")
                continue
            else:
                global_flag = False

        if command == "p":
            print(f"\nКоманда: {command} - позволяет узнать человека по номеру документа.")
            document_number = str(input("Введите номер документа: "))
            name = get_name_by_document(document_number)

            print("-" * 40)
            if name is not None:
                print(f"Документ под номером '{document_number}' принадлежит '{name}'.")
            else:
                print(f"Документа с номером '{document_number}' не существует!")

        elif command == "l":
            print("\nСписок доступных документов:")
            print("-" * 40)
            for doc in get_all_documents():
                print(doc)

        elif command == "s":
            print(f"\nКоманда {command} - позволяет узнать расположение документа по его номеру.")
            document_number = str(input("Введите номер документа: "))
            shelf_number = get_place_document(document_number)

            print("-" * 40)
            if shelf_number is not None:
                print(f"Документ под номером '{document_number}' находится на полке - '{shelf_number}'.")
            else:
                print(f"Документ под номером '{document_number}' не содержится в картотеке.")

        elif command == "a":
            print(f"\nКоманда {command} - позволяет добавить новый документ.")
            print("-" * 45)
            document_type = input("Введите тип документа (passport, invoice, etc): ")
            document_number = input("Введите номер документа: ")
            document_owner = input("Введите владельца документа: ")

            shelf_number = None
            shelf_flag = True
            while shelf_flag:
                shelf_number = input(f"Введите номер полки, на которую хотите поместить дело (сейчас полок: {len(directories)}): ")
                if int(shelf_number) > len(directories) or int(shelf_number) == 0 :
                    print(f"Всего доступно полок - {len(directories)}")
                    continue
                else:
                    shelf_flag = False

            print(add_new_document(document_type, document_number, document_owner, shelf_number))

        elif command == "d":
            print(f"\nКоманда {command} - позволяет удалить существующий документ отовсюду.")
            print("-" * 45)
            document_number = str(input("Введите номер документа: "))
            print(del_document(document_number))

        elif command == "m":
            print(f"\nКоманда {command} - позволяет переместить документ на нужную полку.")
            print("-" * 45)
            document_number = str(input("Введите номер документа: "))

            shelf_number = None
            shelf_flag = True
            while shelf_flag:
                shelf_number = input(
                    f"Введите номер полки, на которую хотите поместить дело (сейчас полок: {len(directories)}): ")
                if int(shelf_number) > len(directories) or int(shelf_number) == 0:
                    print(f"Всего доступно полок - {len(directories)}")
                    continue
                else:
                    shelf_flag = False

            print(move_document(document_number, shelf_number))

        elif command == "as":
            print(f"\nКоманда {command} - позволяет добавить новую полку.")
            print("-" * 45)

            temp_shelf = str()
            for directory in directories.keys():
                temp_shelf += f'{directory}, '

            shelf_number = None
            shelf_flag = True
            while shelf_flag:
                shelf_number = input(f"Введите номер новой полки (уже есть: {temp_shelf[:-2]}): ")
                if shelf_number in temp_shelf:
                    print(f"Введите номер отличный от существующих - {temp_shelf[:-2]}")
                    continue
                else:
                    shelf_flag = False

            print(add_new_place(shelf_number))

        end_program = input("Хотите завершить работу программы (Да/Нет)? ")
        if end_program.capitalize() == "Да":
            main_flag = False

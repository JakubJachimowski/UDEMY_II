from modules import Calendarium
import time

time = time.strftime("%d.%m.%Y, %H:%M")
print(time)

print("""This is going to be an application combining a calendar with to-do app
Viable commands:
- create
- add
- delete
- show
- count
- exit""")

# default list
# user1_list = ['test1', 'test2', 'test3']
# print("Length of the test list: ", len(user1_list))


while True:

    user_input = input("> ").strip().lower()

    match user_input:

        case "create":
            try:
                new_list_name = input(">> Enter name of new list: ")
                user_list = []
                Calendarium.create_file(file=user_list, filepath=f"files/{new_list_name}.txt")
            except FileExistsError:
                print(">>> The list already exists")

        case "add":
            try:
                user_list = Calendarium.open_file()

                new_to_do = input(">> Enter next position: ")
                user_list.append(new_to_do + "\n")

                Calendarium.save_file(file=user_list)

                print(">>> Position added")

            except FileNotFoundError:
                print("File not found")
                continue

        case "show":
            try:
                user_list = Calendarium.open_file()

                for number, item in enumerate(user_list):
                    item = item.strip("\n")
                    print(f"{number + 1}. {item.title()}")

            except FileNotFoundError:
                print("File not found")
                continue

        case "delete":
            try:
                user_list = Calendarium.open_file()

                to_delete = input(">> Delete position: ")
                if to_delete.isdigit():
                    if int(to_delete) <= len(user_list):
                        del user_list[int(to_delete) - 1]
                        print(">>> Position deleted")
                    else:
                        print("*error 1*")
                else:
                    print("*error 2*")

                Calendarium.save_file(file=user_list)

            except FileNotFoundError:
                continue

        case "edit":
            try:
                user_list = Calendarium.open_file()

                to_edit_num = input(">> Edit position: ")
                if to_edit_num.strip():
                    to_edit_txt = input(">>> Enter edit: ")
                    user_list[int(to_edit_num) - 1] = to_edit_txt + "\n"
                    print(">>> Position edited")
                else:
                    print("*error 3*")

                Calendarium.save_file(file=user_list)

            except FileNotFoundError:
                continue

        case "count":
            try:
                user_list = Calendarium.open_file()

                print(f"List contains {len(user_list)} positions")
            except FileNotFoundError:
                continue

        case "exit":
            break

        case _:
            print("* incorrect input *")

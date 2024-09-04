print("""This is going to be an application combining a calendar with to-do app
Viable commands:
- add
- delete
- show
- count
- exit""")

# default list
user1_list = ['test1', 'test2', 'test3']


# print("Length of the test list: ", len(user1_list))


def open_file(filepath):
    with open(filepath, "r") as file_local:
        local_user_list = file_local.readlines()
    return local_user_list


def save_file(filepath, file):
    with open(filepath, "w") as file_local:
        file_local.writelines(file)


while True:

    user_input = input("> ").strip().lower()

    match user_input:

        case "add":
            try:
                user_list = open_file(filepath="files/user_list.txt")

                new_to_do = input(">> Enter next position: ")
                user_list.append(new_to_do + "\n")

                save_file(filepath="files/user_list.txt", file=user_list)

                print(">>> Position added")

            except FileNotFoundError:
                print("File not found")
                continue

        case "show":
            try:
                user_list = open_file(filepath="files/user_list.txt")

                for number, item in enumerate(user_list):
                    item = item.strip("\n")
                    print(f"{number + 1}. {item.title()}")

            except FileNotFoundError:
                print("File not found")
                continue

        case "delete":
            try:
                user_list = open_file(filepath="files/user_list.txt")

                to_delete = input(">> Delete position: ")
                if to_delete.isdigit():
                    if int(to_delete) <= len(user_list):
                        del user_list[int(to_delete) - 1]
                        print(">>> Position deleted")
                    else:
                        print("*error 1*")
                else:
                    print("*error 2*")

                save_file(filepath="files/user_list.txt", file=user_list)

            except FileNotFoundError:
                continue

        case "edit":
            try:
                user_list = open_file(filepath="files/user_list.txt")

                to_edit_num = input(">> Edit position: ")
                if to_edit_num.strip():
                    to_edit_txt = input(">>> Enter edit: ")
                    user_list[int(to_edit_num) - 1] = to_edit_txt + "\n"
                    print(">>> Position edited")
                else:
                    print("*error 3*")

                save_file(filepath="files/user_list.txt", file=user_list)

            except FileNotFoundError:
                continue

        case "count":
            try:
                user_list = open_file(filepath="files/user_list.txt")

                print(f"List contains {len(user_list)} positions")
            except FileNotFoundError:
                continue

        case "exit":
            break

        case _:
            print("* incorrect input *")

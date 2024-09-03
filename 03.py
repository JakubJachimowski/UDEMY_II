print("""This is going to be an application combining a calendar with to-do app
Viable commands:
- add
- delete
- show
- count
- exit""")

# default list
user1_list = ['test1', 'test2', 'test3']
print(len(user1_list))


while True:

    user_input = input("> ").strip().lower()

    match user_input:

        case "add":
            to_do_position = input(">> Enter next position: ")
            user1_list.append(to_do_position)
            print(f"Task \"{to_do_position}\" added to the list")

        case "show":
            if user1_list:
                for number, item in enumerate(user1_list):
                    print(f"{number + 1}. {item.title()}")
            else:
                print("* there are no positions to display *")

        case "delete":
            if user1_list:
                for number, item in enumerate(user1_list):
                    print(f"{number + 1}. {item.title()}")
                print("Which position do you wish to remove?")
                remove_number = input(">> ")
                if remove_number.isdigit():
                    if int(remove_number) <= len(user1_list):
                        del user1_list[int(remove_number) - 1]
                    else:
                        print("* invalid position *")
                else:
                    print("* invalid input *")

        case "edit":
            if user1_list:
                for number, item in enumerate(user1_list):
                    print(f"{number + 1}. {item.title()}")
                print("Which position do you wish to edit?")
                edit_number = input(">> ")
                if edit_number.isdigit():
                    if int(edit_number) <= len(user1_list):
                        corrected_position = input("Enter correct position: ")
                        user1_list[int(edit_number) - 1] = corrected_position
                    else:
                        print("* invalid position *")
                else:
                    print("* invalid input *")

        case "count":
            print(f"The list contains {len(user1_list)} positions.")

        case "exit":
            break

        case _:
            print("* incorrect input *")

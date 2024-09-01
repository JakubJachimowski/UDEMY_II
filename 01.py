print("""This is going to be an application combining a calendar with to-do app
Viable commands:
- add
- delete
- show
- count
- exit""")

# default list
user1_list = [1, 2, 3]


def user_input():
    x = input("> ")
    x = x.upper()
    return x


def next_position():
    y = input("> ")
    y = y.title()
    return y


while True:

    word = user_input()
    if word == "ADD":
        print("ENTER POSTION: ")
        position = next_position()
        user1_list.append(position)
        print("'", position, "'", "has been added.")

    elif word == "DELETE":
        user1_list = []
        print("The list is empty.")

    elif word == "SHOW":
        print("Current list: ", user1_list)

    elif word == "COUNT":
        print("Current list contains", len(user1_list), "positions.")

    elif word == "EXIT":
        break

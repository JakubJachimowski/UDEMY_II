FILEPATH = "files/user_list.txt"


def open_file(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        user_list = file_local.readlines()
    return user_list


def save_file(file, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(file)


def create_file(file, filepath):
    with open(filepath, "w") as file_local:
        file_local.writelines(file)
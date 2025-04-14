def Todo_read():
    with open("Todos.txt", 'r') as file:
        list = file.readlines()
    return list

def Todo_write(Todo_list):
    with open("Todos.txt", 'w') as file:
        for item in Todo_list:
            file.writelines(item)
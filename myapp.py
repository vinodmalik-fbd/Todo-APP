
from Functionpy import Todo_read, Todo_write
import time
import FreeSimpleGUI as sg
now = time.strftime("%D %T")
print("it is", now)

# Using FreeSimpleGUI package to develop GUI
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("My TODO list",layout=[[label],[input_box,add_button]])
window.read()
window.close()

while True:
    user_input = input("Please enter your choice add/show/complete/exit:")
    user_input = user_input.strip()

    if  user_input.startswith("add"):
        todo = input("Enter the todo:")
        Todos = Todo_read()
        Todos.append(todo + '\n')
        Todo_write(Todos)

    elif user_input.startswith("complete"):
            with open("Todos.txt", 'r') as file:
                list = file.readlines()
            for index, item in enumerate(list):
                item = item.strip()
                raw = f'{index + 1}-{item}'
                print(raw)
            index = int(input("Enter todo number you want to complete:"))
            list.pop(index - 1)
            with open("Todos.txt", 'w') as file:
                for item in list:
                    file.writelines(item)

    elif user_input.startswith("show"):
        with open("Todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip()
            raw = f'{index + 1}-{item}'
            #    print(index,'-',item)
            print(raw)
        # print(file.readlines())
        file.close()

    elif user_input.startswith("edit"):

        index = int(input("Enter the todo to be edited:"))
        todo = input("Enter the new todo:")
        with open("Todos.txt", 'r') as file:
            todos = file.readlines()
    # todos.pop(index-1)
        todos[index - 1] = todo

        with open("Todos.txt", 'w') as file:
            for item in todos:
                item = item.strip()
                file.writelines(item + '\n')

    elif user_input.startswith("exit"):
        break

    else:
        print("Wrong choice")

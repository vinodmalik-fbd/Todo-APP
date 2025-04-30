
import Functionpy
import time
import FreeSimpleGUI as sg
now = time.strftime("%D %T")
print("it is", now)

# Using FreeSimpleGUI package to develop GUI for list
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values= Functionpy.Todo_read(),key='todos',
                      enable_events=True,size=[45,10])
add_button = sg.Button("Add")
add_button1 = sg.Button("Show")
add_button2 = sg.Button("Edit")
add_button3 = sg.Button("Complete")
window = sg.Window("My TODO list",layout=[[label],[input_box,add_button,add_button1,add_button3],[list_box,add_button2]],
                   font=('Helvetica', 20))
while True:
    event, value = window.read()
    print(event)
    print(value["todo"])
    print(value["todos"])
    match event:
        case "Add":
            Todolist = Functionpy.Todo_read()
            newtodo = value["todo"]
            Todolist.append(newtodo + '\n')
            Functionpy.Todo_write(Todolist)
            window['todos'].update(values=Todolist)

        case "Show":
            Todolist = Functionpy.Todo_read()
            for index,item in enumerate(Todolist):
                print(index+1,'-',item.strip())

        case "Complete":
            Todolist = Functionpy.Todo_read()
            Todolist.pop(int(value["todo"]))
            Functionpy.Todo_write(Todolist)

        case "Edit":
            Todolist = Functionpy.Todo_read()
            todo_to_edit = value['todos'][0]
            new_todo = value['todo']
            index = Todolist.index(todo_to_edit)
            Todolist[index] = new_todo + '\n'
            Functionpy.Todo_write(Todolist)
            window['todos'].update(values=Todolist)

        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()

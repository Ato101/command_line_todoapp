from function import get_todos,write_todos
import time
print("hello")
now = time.strftime('%b %d,%Y %H:%M %S')
print("it is ",now)
while True:
     user_action = input("add,show ,edit,complete or exits: ")
     user_action = user_action.strip()

     if user_action.startswith('add'):
          todo= user_action[4:]
          new_todo = todo+'\n'

          todos= get_todos('todos.txt')

          todos.append(new_todo)

          write_todos(todos,'todos.txt')


     elif user_action.startswith('show'):
          todos = get_todos("todos.txt")
          for index, items in enumerate(todos):
               item= items.strip('\n').capitalize()
               row = f"{index+1}-{item}"
               print(row)


     elif  user_action.startswith('edit') :
          try:
               number = int(user_action[5])
               update_number= number-1

               todos = get_todos('todos.txt')

               update = input('Enter the new todo item:')+'\n'
               todos[update_number] = update

               write_todos(todos,'todos.txt')


          except ValueError:
               print('your command is not valid')
               continue



     elif user_action.startswith('complete'):
          try:
               number = int(user_action[9:])
               todos = get_todos('todos.tx')

               number=number-1
               todos.pop(number)

               write_todos(todos,'todos.txt')
          except IndexError:
               print('Out of range')
               continue


     elif 'exist' in user_action:
         break

print('bye')

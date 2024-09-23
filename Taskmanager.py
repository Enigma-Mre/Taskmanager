
# Retreive user log in data:

username_list = []
password_list = []

log_in = open("user.txt", "r")

for user in log_in:
    user = user.strip()
    user = user.split(", ")

    username_list.append(user[0])
    password_list.append(user[1])
log_in.close()

# Menu options:

user_menu = ('''\nPlease select one of the following options:
             va - view all tasks
             vm - view my tasks
             e - exit
             : ''')

admin_menu = ('''\nPlease select one of the following options:
             r - register a user
             a - add task
             va - view all tasks
             vm - view my tasks
             e - exit
             : ''')

# User log in:
# This will allow the user to log in determine if user input is correct or incorrect.

user_log = False

print("\nGreetings and welcome to the employee task and registration menu!")
while not user_log:
    username = input("\nPlease enter your username: ")
    password = input("\nPlease enter your password: ")

    if (username in username_list) and (password in password_list) and (username_list.index(username)) == (password_list.index(password)):
        user_log = True
        if username == "admin":
            print(admin_menu)
        else:
            print(user_menu)

    elif username not in username_list:
        print("\nInvalid username.")
        
    elif password not in password_list:
        print("\nInvalid password.")

    else:
        print("\nInvalid username and password.")

# Admin menu selections:
# The admin menu selections will allow the admin to register a new user, add a new task and all other fetures.

menu = ""

while menu != "e":
    menu = input("\nWhat would you like to do from the menu selection: ")
    
    if menu == 'r':
        new_username = input("\nPlease enter new username: ")
        new_password = input("\nPlease enter new user password: ")
        password_confirm = input("\nPlease confirm password: ")

        if new_username in username_list:
            print("\nThis username already exists.")

        elif new_password in password_list:
            print("\nThis password is already taken.")

        else:
            log_in = open("user.txt", "a")
            log_in.write(f"\n{new_username}, {new_password}")
            log_in.close()


# Add new task option:
# This will allow admin to add a new user, task, task discription, due date and current date.

    elif menu == "a":
        task_user = input("\nEnter the name of the person assigned to this task: ")
        task_title = input("\nEnter the title of this task: ")
        task_disc = input("\nEnter a description of the task: ")
        due_date = input("\nWhen due date of this task: ")
        current_date = input("\nPlease enter the current date: ")
        tasks_completion = input("\nIs the task complete: ")

        task = open("task.txt", "a")
        task.write(f"\n{task_user}, {task_title}, {task_disc}, {due_date}, {current_date}, {tasks_completion}")
        task.close()

# View all tasks option:
# This will allow the admin/user to view all tasks, who their assigned to, the due dates, the current date, and if it is completed.

    elif menu == "va":
        tasks = open("task.txt", "r")
        for line in tasks:
            line = line.strip()
            line = line.split(", ")
            
            i = 0
            print("_______________________________________\n")
            for items in line:
                if i == 0:
                    print(f"Assigned to:        {items}")
                    i += 1
                elif i == 1:
                    print(f"Task title:         {items}")
                    i += 1
                elif i == 2:
                    print(f"Task description:   {items}")
                    i += 1
                elif i == 3:
                    print(f"Due date:           {items}")
                    i += 1
                elif i == 4:
                    print(f"Date assigned:      {items}")
                    i += 1
                elif i == 5:
                    print(f"Task complete:      {items}")
                    i += 1
            print("_______________________________________\n")
        tasks.close()

# View my taks menu option:
# This will allow a single admin/user to look at all the work that is assigned to them.
    
    elif menu == 'vm':
        user = input("\nPlease confirm your username: ")
        tasks = open("task.txt", "r")
        
        for line in tasks:
            if user in line:
                line = line.split(", ")
                
                i = 0
                print("_______________________________________\n")
                for items in line:
                    if i == 0:
                        print(f"Assigned to:        {items}")
                        i += 1
                    elif i == 1:
                        print(f"Task title:         {items}")
                        i += 1
                    elif i == 2:
                        print(f"Task description:   {items}")
                        i += 1
                    elif i == 3:
                        print(f"Due date:           {items}")
                        i += 1
                    elif i == 4:
                        print(f"Date assigned:      {items}")
                        i += 1
                    elif i == 5:
                        print(f"Task complete:      {items}")
                        i += 1
                print("_______________________________________\n")  
        tasks.close()
# This will allow the admin to exit the menu.

    elif menu == 'e':
        print("\nGoodbye and thank you for using the employee menu!")
        exit()

    else:
        print("You have entered an invalid input. Please try again.")

# If you are an admin you will receive access to the full menu, else you will be limited to the user menu.
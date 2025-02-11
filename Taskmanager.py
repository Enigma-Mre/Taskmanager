
# User data.
# This is a function that will find and pull the user data and infomation from the txt files.

import datetime
from datetime import date

username_list = []
password_list = []

log_in = open("user.txt", "r")

for user in log_in:
    user = user.strip()
    user = user.split(", ")

    username_list.append(user[0])
    password_list.append(user[1])
log_in.close()

# User login.
# This is a function that will allow the user to login to the application.

def user_login():
    user_log = False

    print("\nGreetings and welcome to the task manager application login!")
    while not user_log:
        username = input("\nPlease enter your username: ")
        password = input("\nPlease enter your password: ")

        if (username in username_list) and (password in password_list) and (username_list.index(username)) == (password_list.index(password)):
            user_log = True
            return(menu_options(username))

        elif username not in username_list:
            print("\nInvalid username.")
            
        elif password not in password_list:
            print("\nInvalid password.")

        else:
            print("\nInvalid username and password.")

# Menu options.
# This is function that will print the menu options depending on the username that u give.

def menu_options(username):
    if username == "admin":
        print('''\nPlease select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                gr - generate reports
                ds - display statistics
                e - exit
                : ''')
        menu = input("\nWhat would you like to do from the select menu: ")
        if menu == "r":
             return reg_user(username)
        elif menu == "a":
             return add_task()
        elif menu == "va":
             return view_all()
        elif menu == "vm":
             return view_mine()
        elif menu == "gr":
             return gen_reports()
        elif menu == "ds":
             return dis_statistics()
        elif menu == "e":
             return exit_program()
        else:
             print("\nYou have entered an invlaid input.")
        
    else:
        print('''\nPlease select one of the following options:
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : ''')
        menu = input("\nWhat would you like to do from the select menu: ")
        if menu == "va":
             return view_all()
        elif menu == "vm":
             return view_mine()
        elif menu == "e":
             return exit_program()
        else:
             print("\nYou have entered an invlaid input.")

# Register user.
# This function will allow the admin to register a new user.

def reg_user(username):
    if username == "admin":
        new_username = input("\nPlease enter new username: ")
        new_password = input("\nPlease enter new user password: ")

        while new_username in username_list:
                print("\nThis username already exists.")
                new_username = input("\nPlease enter new username: ")

        while new_password in password_list:
            print("\nThis password is already taken.")
            new_password = input("\nPlease enter new user password: ")

        password_confirm = input("\nPlease confirm your password: ")
        while password_confirm != new_password:
                password_confirm = input("\nPasswords do not match, please try again: ")

        log_in = open("user_overview.txt", "a")
        log_in.write(f"\n{new_username}, {new_password}")
        log_in.close()
        print("\nNew user successfully added!")
        print(menu_options(username))
    
    else:
        print("\nCannot complete proccess, you are not an admin.")
            
# Add task.
# This is a function that allows the admin to add a new task.

def add_task():
    task_number = input("\nPlease enter the number of this task: ")
    task_user = input("\nEnter the name of the person assigned to this task: ")
    task_title = input("\nEnter the title of this task: ")
    task_disc = input("\nEnter a description of the task: ")
    due_date = input("\nWhen due date of this task: ")
    current_date = input("\nPlease enter the current date: ")
    tasks_completion = input("\nIs the task complete: ")

    task = open("Taskmanager/user_overview.txt", "a")
    task.write(f"\n{task_number},{task_user}, {task_title}, {task_disc}, {due_date}, {current_date}, {tasks_completion.capitalize()}")
    task.close()

# View all tasks option.
# This is a function that will allow the user/admin to view all tasks.

def view_all():
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

# View my tasks.
# This is a function that will allow the user/admin to view all of there assigned tasks.

def view_mine():
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

# Generate reports.

def gen_reports():
    # Task overview:
    task_overview = open("user_overview.txt", "a")

    print("\nGenerated Report to task_overview.txt and user_overview.txt")

    task_count = open("task.txt", "r")
    total = len(task_count.readlines())
    task_overview.write(f"\nThe total number of tasks is: {total}.\n")
    task_count.close()

    tasks_completion = open("task.txt", "r")
    count_complete = 0
    count_incomplete = 0

    for line in tasks_completion:
        line = line.strip()
        line = line.split(", ")
        if "Yes" in line:
            count_complete += 1
        elif "No" in line:
            count_incomplete += 1

    task_overview.write(f"The number of completed tasks is {count_complete}\n")
    task_overview.write(f"The number of incomplete tasks is {count_incomplete}\n")
    tasks_completion.close()

    tasks_overdue = open("task.txt", "r")

    count_overdue = 0

    for line in tasks_overdue:
        line = line.strip()
        line = line.split(", ")

        current_date = date.today()
        due_date = datetime.datetime.strptime(line[4], "%d %b %Y")
        due_date = due_date.date()

        if due_date < current_date:
            if line[5] == "No":
                count_overdue += 1

    task_overview.write(f"The number of tasks that are overdue and incomplete is: {count_overdue}\n")

    incomplete_per = (count_incomplete / total) * 100
    task_overview.write(f"The percentage of tasks that are incomplete: {incomplete_per:.2f}%.\n")

    overdue_per = (count_overdue / total) * 100
    task_overview.write(f"The percentage of tasks that are overdue: {overdue_per:.2f}%\n")

    task_overview.close()

    # User overview:
    # Total registered users & total tasks:
    user_overview = open("user_overview.txt", "w")

    user_overview.write(f"The number of users registered within this application: {len(username_list)}\n")

    user_task_count = open("task.txt", "r")
    total_tasks_user = len(user_task_count.readlines())
    user_overview.write(f"The total number of tasks is: {total_tasks_user}\n"
                        f"\n"
                        f"\n")
    user_task_count.close()

    # For each user Task information:
    user_per_tasks = open("task.txt", "r")

    for user in username_list:

        # Total number of tasks assigned to a user:
        task_user = open("task.txt", "r")
        user_total_tasks = 0

        for task in task_user:
            task = task.strip()
            task = task.split(", ")

            if user == task[0]:
                user_total_tasks += 1
        user_overview.write(f"username: {user}\n")
        user_overview.write(f"The total number of tasks assigned to {user}: {user_total_tasks}\n")
        task_user.close()

        user_per_tasks = open("task.txt", "r")

        user_total_tasks = 0
        user_completed = 0
        user_incomplete = 0
        user_over_incomplete = 0

        for task in user_per_tasks:
            task = task.strip()
            task = task.split(", ")

            if user == task[0]:
                user_total_tasks += 1

                if task[5] == "Yes":
                    user_completed += 1
                elif task[5] == "No":
                    user_incomplete += 1
                    
                    # Check overdue tasks:
                    current_date = date.today()
                    due_date = datetime.datetime.strptime(task[4], "%d %b %Y")
                    due_date = due_date.date()
                    if due_date < current_date:
                        user_over_incomplete += 1

        user_task_per = (user_total_tasks / total_tasks_user) * 100
        user_overview.write(f"The percentage of total tasks assigned to {user}: {user_task_per:.2f}%\n")

        user_completed_per = (user_completed / user_total_tasks) * 100
        user_overview.write(f"The percentage of total completed tasks assigned to {user}: {user_completed_per:.2f}%\n")

        user_incomplete_per = (user_incomplete / user_total_tasks) * 100
        user_overview.write(f"The percentage of total incomplete tasks assigned to {user}: {user_incomplete_per:.2f}%\n")

        user_over_incomplete_per = (user_over_incomplete / user_total_tasks) * 100
        user_overview.write(
            f"The percentage of total incomplete and overdue tasks assigned to {user}: {user_over_incomplete_per:.2f}%\n"
            f"\n"
            f"\n")

    user_per_tasks.close()
    user_overview.close()

# Display statistics:
# This function will display the statistics of the general report.

def dis_statistics():
    with open("user_overview.txt", "r") as task_o:
        raw_contents1 = task_o.read()
        print("_______________________________________\n")
        print(raw_contents1)
        print("_______________________________________\n")
    with open("user_overview.txt", "r") as user_o:
        raw_contents2 = user_o.read()
        print(raw_contents2)
        print("_______________________________________\n")
    task_o.close()
    user_o.close()

# Exit the program.
# This is a function that will allow the user/admin to exit the program.

def exit_program():
        print("\nGoodbye and thank you for using the employee menu!")
        exit()

# start program

print(user_login())

#'''

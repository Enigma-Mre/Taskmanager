# Taskmanager

## Table of Contents

2. [Project Description](#project-description)
   - [Importance](#importance)
   - [Functionality](#functionality)
3. [Installation Instructions](#installation-instructions)
4. [Usage Instructions](#usage-instructions)
   - [Starting the Application](#starting-the-application)
   - [Menu Options](#menu-options)
   - [Example Workflows](#example-workflows)
7. [File Operations](#file-operations)
   - [User Management](#user-management)
   - [Task Management](#task-management)
8. [Viewing Tasks](#viewing-tasks)
   - [View All Tasks](#view-all-tasks)
   - [View My Tasks](#view-my-tasks)
10. [Exit Procedure](#exit-procedure)


## Project Description

This project is a task management and user registration system designed for efficient tracking and assignment of tasks within an organization. It allows users to log in with their credentials, view tasks assigned to them, and enables administrators to manage user registrations and task assignments effectively.

### Importance

In today's fast-paced work environments, effective task management is crucial for enhancing productivity and ensuring that deadlines are met. This system streamlines the process by providing an intuitive interface for both users and administrators, helping teams to stay organized and focused on their goals.

### Functionality

- **User Authentication**: Secure login for users and administrators.
- **Task Management**: Administrators can register new users and assign tasks, while users can view their assigned tasks.
- **Task Tracking**: Users can monitor task progress, due dates, and completion status.

This project aims to improve collaboration and accountability in task management, making it an essential tool for any organization.


## Installation Instructions

To install and run this project locally, follow these steps:

### Prerequisites

- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- You will also need a text editor or IDE (like Visual Studio Code, PyCharm, or any text editor of your choice) to edit the code.

### Steps to Install

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone [[repository-url]](https://github.com/Enigma-Mre/Taskmanager/edit/main/README.md)
   ```

2. **Navigate to the Project Directory**:
   Change into the project directory:
   ```bash
   cd [project-directory]
   ```

3. **Create Required Files**:
   Ensure you have the necessary text files (`user.txt` and `task.txt`) in the project directory. You can create empty files using the following commands:
   ```bash
   touch user.txt
   touch task.txt
   ```

4. **Run the Application**:
   Start the program by executing:
   ```bash
   python Taskmanager.py
   ```

5. **Follow On-Screen Instructions**:
   After running the script, follow the prompts in the console to interact with the application.
   

## Usage Instructions

After successfully installing the project, follow these steps to use it effectively:

### Starting the Application

1. **Run the Program**:
   Open your terminal, navigate to the project directory, and execute:
   ```bash
   python Taskmanager.py
   ```

2. **Log In**:
   Upon starting the application, you will see a prompt to enter your username and password. Enter your credentials:
   ![Login](https://github.com/user-attachments/assets/2f9ba54a-c7fd-4ff4-b59e-0ba403e411c0)


### Menu Options

After logging in, you will be presented with the appropriate menu based on your user type (user or admin).

- **User Menu**:
  - **View All Tasks** (`va`): Displays all tasks in the system.
  - **View My Tasks** (`vm`): Shows tasks assigned specifically to you.
  - **Exit** (`e`): Logs you out of the application.

  ![UserMenu](https://github.com/user-attachments/assets/17fd5ccf-7999-4aa9-b5c8-2a5eb9b6cccc)


- **Admin Menu** (for admin users):
  - **Register a User** (`r`): Allows the admin to add new users.
  - **Add Task** (`a`): Enables the admin to assign new tasks.
  - **View All Tasks** (`va`): Same as above.
  - **View My Tasks** (`vm`): Same as above.
  - **Exit** (`e`): Logs you out of the application.

  ![AdminMenu](https://github.com/user-attachments/assets/3d836cb7-d03f-4b19-9399-adf41640e514)


### Example Workflows

1. **Register a New User**:
   - Select the `r` option from the admin menu.
   - Follow the prompts to enter the new user's username and password.

   ![RegNewUser](https://github.com/user-attachments/assets/6ffa2f5d-11ac-42b4-9696-304136a1a764)


2. **Add a New Task**:
   - Select the `a` option from the admin menu.
   - Fill in the task details when prompted.

   ![AddNewTask](https://github.com/user-attachments/assets/948b461e-ca79-42b8-af4a-487912dc8fcf)


3. **View Tasks**:
   - Select either `va` or `vm` to view all tasks or just your assigned tasks.
   - The application will display task details, including assignee, title, description, due date, and completion status.

   ![ViewTasks](https://github.com/user-attachments/assets/22b2488f-d3a1-4e9f-a697-b5db7c4de10e)


### Exiting the Application

To exit the application at any time, select the `e` option from the menu.


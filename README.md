# Taskmanager

## Table of Contents


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
   ![Login Screen](path/to/screenshot1.png)

### Menu Options

After logging in, you will be presented with the appropriate menu based on your user type (user or admin).

- **User Menu**:
  - **View All Tasks** (`va`): Displays all tasks in the system.
  - **View My Tasks** (`vm`): Shows tasks assigned specifically to you.
  - **Exit** (`e`): Logs you out of the application.

  ![User Menu](path/to/screenshot2.png)

- **Admin Menu** (for admin users):
  - **Register a User** (`r`): Allows the admin to add new users.
  - **Add Task** (`a`): Enables the admin to assign new tasks.
  - **View All Tasks** (`va`): Same as above.
  - **View My Tasks** (`vm`): Same as above.
  - **Exit** (`e`): Logs you out of the application.

  ![Admin Menu](path/to/screenshot3.png)

### Example Workflows

1. **Register a New User**:
   - Select the `r` option from the admin menu.
   - Follow the prompts to enter the new user's username and password.

   ![Register User](path/to/screenshot4.png)

2. **Add a New Task**:
   - Select the `a` option from the admin menu.
   - Fill in the task details when prompted.

   ![Add Task](path/to/screenshot5.png)

3. **View Tasks**:
   - Select either `va` or `vm` to view all tasks or just your assigned tasks.
   - The application will display task details, including assignee, title, description, due date, and completion status.

   ![View Tasks](path/to/screenshot6.png)

### Exiting the Application

To exit the application at any time, select the `e` option from the menu.


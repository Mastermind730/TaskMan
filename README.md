# TaskMan

TaskMan is a Django-based task management application that allows users to track and manage tasks. The application includes features like user authentication, task creation, task status updates, and an activity feed to track user actions.

## Features

- **User Authentication**
  - Sign up with username, email, and password
  - Login with email and password
  - Logout functionality

- **Task Management**
  - View all tasks created by the user
  - Add new tasks with a name and deadline
  - Mark tasks as complete or incomplete
  - Delete existing tasks
  - Sort tasks by name, completion date, or creation date

- **Activity Feed**
  - View a list of recent actions, such as task creation, completion, and deletion
  - All timestamps are in the format `DD MON, YYYY HH:MM`

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (default Django database)
- **Others**: FontAwesome for icons

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/taskman.git
   cd taskman

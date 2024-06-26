## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jahirulalam42/TeamCollab.git
   cd project_management/

  2. Install dependencies:

pip install -r requirements.txt

3. Apply database migrations:

python manage.py migrate

Run the Django development server:

python manage.py runserver



 API Documentation

## API Endpoints

### Users

- **Register User**
  - `POST /api/users/register/`: Create a new user.

- **Login User**
  - `POST /api/users/login/`: Authenticate a user and return a token.

- **Get User Details**
  - `GET /api/users/{id}/`: Retrieve details of a specific user.

- **Update User**
  - `PUT/PATCH /api/users/{id}/`: Update user details.

- **Delete User**
  - `DELETE /api/users/{id}/`: Delete a user account.

### Projects

- **List Projects**
  - `GET /api/projects/`: Retrieve a list of all projects.

- **Create Project**
  - `POST /api/projects/`: Create a new project.

- **Retrieve Project**
  - `GET /api/projects/{id}/`: Retrieve details of a specific project.

- **Update Project**
  - `PUT/PATCH /api/projects/{id}/`: Update project details.

- **Delete Project**
  - `DELETE /api/projects/{id}/`: Delete a project.

### Tasks

- **List Tasks**
  - `GET /api/projects/{project_id}/tasks/`: Retrieve a list of all tasks in a project.

- **Create Task**
  - `POST /api/projects/{project_id}/tasks/`: Create a new task in a project.

- **Retrieve Task**
  - `GET /api/tasks/{id}/`: Retrieve details of a specific task.

- **Update Task**
  - `PUT/PATCH /api/tasks/{id}/`: Update task details.

- **Delete Task**
  - `DELETE /api/tasks/{id}/`: Delete a task.

### Comments

- **List Comments**
  - `GET /api/tasks/{task_id}/comments/`: Retrieve a list of all comments on a task.

- **Create Comment**
  - `POST /api/tasks/{task_id}/comments/`: Create a new comment on a task.

- **Retrieve Comment**
  - `GET /api/comments/{id}/`: Retrieve details of a specific comment.

- **Update Comment**
  - `PUT/PATCH /api/comments/{id}/`: Update comment details.

- **Delete Comment**
  - `DELETE /api/comments/{id}/`: Delete a comment.

This is a simple Flask application for learning CRUD operations at a foundational level. 
It defines several REST endpoints to carry out operations. 
It stores data in a simple relational database with one model (defined using SQLAlchamy). 

# **Requirements**
- Python 3.11
- Poetry

# **API Endpoints**

#### 1. GET `/contacts`
- **Description:** Retrieves all contacts from the database.
- **Returns:** JSON list of all contacts.

#### 2. POST `/create_contact`
- **Description:** Creates a new contact.
- **JSON Body Required:** 
  ```json
  {
    "firstName": "First Name",
    "lastName": "Last Name",
    "email": "email@example.com"
  }
  ```
- **Returns:** Message indicating if the user was created or if an error occurred.

#### 3. PATCH `/update_contact/<int:user_id>`
- **Description:** Updates an existing contact.
- **Parameters:** `user_id` - The ID of the contact.
- **JSON Body (Optional Fields):**
  ```json
  {
    "firstName": "New First Name",
    "lastName": "New Last Name",
    "email": "new.email@example.com"
  }
  ```
- **Returns:** Message indicating if the user was updated or if the user was not found.

#### 4. DELETE `/delete_contact/<int:user_id>`
- **Description:** Deletes a contact.
- **Parameters:** `user_id` - The ID of the contact.
- **Returns:** Message indicating if the user was deleted or if the user was not found.

# **Tech Stack**


- **[Python](https://www.python.org/)**: A versatile programming language that is easy to learn and powerful in execution. It's used for all backend logic.

- **[Poetry](https://python-poetry.org/)**: A tool for dependency management and packaging in Python. It helps manage libraries and dependencies with ease and reproducibility.

- **[Flask](https://flask.palletsprojects.com/)**: A lightweight and flexible Python web framework. It provides tools and features to create and deploy web applications quickly.

- **[SQLAlchemy](https://www.sqlalchemy.org/)**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python. It allows the application to communicate with the database using Python code instead of SQL.

# **Usage**

## **Install Dependencies**
Install project dependencies using Poetry CLI:

```sh
poetry install
```

> This will automatically create a virtual environment. 

## **Run Project**
Use Poetry to run the project locally:

```sh
poetry run python main.py
```

> Will start the server at localhost:5000
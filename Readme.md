# Django Simple CRUD

A simple project to learn Django by implementing a basic CRUD (Create, Read, Update, Delete) application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-simple-crud.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd django-simple-crud
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On Unix or MacOS
    source env/bin/activate
    ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser to access the Django admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Usage

- **Django Admin:** Access the Django admin interface at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.
- **CRUD Operations:** You can perform basic CRUD operations through the Django admin interface.

## Features

- Basic CRUD functionality for managing database records.
- Django admin interface for managing models.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


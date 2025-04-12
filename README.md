
# Django Library Management System

This is a Django-based web application for managing an online library system. It allows administrators to manage authors, books, and borrow records. Additionally, it includes the feature to export data to Excel.

## Features

- **Author Management**: Add, update, delete, and list authors.
- **Book Management**: Add, update, delete, and list books.
- **Borrow Record Management**: Add, update, delete, and list borrow records.
- **Export to Excel**: Export authors, books, and borrow records to separate Excel sheets.
- **Pagination**: All lists (authors, books, and borrow records) are paginated for easy navigation.
- **User Registration & Login**: Admin users can register and log in.

## Requirements

- Python 3.8 or above
- Django 5.1.4
- openpyxl
- xlwt

## Installation

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/shreyash0019/LiberaryManagement.git
cd LiberaryManagement
```

### Step 2: Set Up a Virtual Environment (Optional but recommended)

Create a virtual environment to manage the project dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

- On Windows:
    ```bash
    venv\Scripts\activate
    ```

### Step 3: Install the Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the required packages using pip:

```bash
pip install django openpyxl xlwt
```

### Step 4: Set Up the Database

Run migrations to set up the database:

```bash
python manage.py migrate
```

### Step 5: Create a Superuser

To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser credentials.

### Step 6: Run the Development Server

Now, you can run the Django development server:

```bash
python manage.py runserver
```

Visit the application in your browser at `http://127.0.0.1:8000/`.

### Step 7: Access the Admin Panel

- Go to the admin panel at `http://127.0.0.1:8000/admin/`.
- Log in with the superuser account you created earlier.

### Step 8: Explore the Features

You can manage authors, books, and borrow records through the admin interface.

- **Authors**: Add, edit, and delete authors.
- **Books**: Add, edit, and delete books.
- **Borrow Records**: Add, edit, and delete borrow records.
- **Export to Excel**: Export authors, books, and borrow records to Excel files.

### Step 9: Additional Features

- You can also view and export the data to Excel by visiting the respective export URLs:
  - **Export Authors**: `/export-authors/`
  - **Export Books**: `/export-books/`
  - **Export Borrow Records**: `/export-borrows/`

## Files and Structure

The project includes the following files:

- **`/manager`**: The app that contains the models, views, forms, and templates.
  - **`models.py`**: Contains the models for Author, Book, and BorrowRecord.
  - **`views.py`**: Contains the views for managing authors, books, and borrow records.
  - **`forms.py`**: Contains forms for adding/editing authors, books, and borrow records.
  - **`urls.py`**: Contains URL routes for the views.
  - **`templates/`**: Contains HTML templates for the web pages.
  
- **`/library/settings.py`**: Django project settings.
- **`requirements.txt`**: The list of required packages for the project.

## Contributing

If you would like to contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.



# Django Library Management System

This is a Django-based web application for managing an online library system. It allows administrators to manage authors, books, and borrow records. Additionally, it includes features like user registration, dashboard, pagination, and exporting data to Excel.

## 🚀 Features

- **Dashboard**: Overview page with motivational quotes.
- **Author Management**: Add, update, delete, and list authors.
- **Book Management**: Add, update, delete, and list books.
- **Borrow Record Management**: Add, update, delete, and list borrow records.
- **Export to Excel**: Export authors, books, and borrow records to Excel.
- **Pagination**: Easy navigation across paginated lists.
- **User Registration**: Admins can register using a dedicated form.
- **Custom Template Filters**: Includes custom filters (e.g., for form styling).

## 📊 Requirements

- Python 3.8 or above
- Django 5.1.4
- openpyxl
- xlwt

## 📖 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/shreyash0019/LiberaryManagement.git
cd LiberaryManagement
```

### Step 2: Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
```
Activate the virtual environment:
- **macOS/Linux**: `source venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

### Step 3: Install the Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
```bash
python manage.py migrate
```

### Step 5: Create a Superuser
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

Visit the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📓 Usage

- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Register: `/register/`
- Dashboard: `/dashboard/`
- Export Authors: `/export-authors/`
- Export Books: `/export-books/`
- Export Borrow Records: `/export-borrows/`

## 📂 Project Structure (Highlights)

```
library/
├── library/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manager/
│   ├── migrations/
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── form_filters.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── manager/
│       ├── add_author.html
│       ├── add_book.html
│       ├── add_borrow.html
│       ├── author_confirm_delete.html
│       ├── author_form.html
│       ├── author_list.html
│       ├── base.html
│       ├── book_confirm_delete.html
│       ├── book_form.html
│       ├── book_list.html
│       ├── borrow_form.html
│       ├── borrow_list.html
│       ├── borrowrecord_confirm_delete.html
│       ├── dashboard.html
│       ├── edit_author.html
│       ├── edit_book.html
│       ├── edit_borrow.html
│       ├── pagination.html
│       └── register.html
├── static/css/style.css
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 📄 Files of Interest

- **`models.py`**: Models for `Author`, `Book`, and `BorrowRecord`
- **`forms.py`**: Django forms for input handling
- **`views.py`**: CRUD and logic views for the app
- **`templatetags/form_filters.py`**: Custom template filters
- **`templates/manager/*.html`**: All UI templates

## 💼 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request

## ✉️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
[Shreyash Ingle](https://github.com/shreyash0019)


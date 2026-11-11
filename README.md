# 💰 Travel Expenses Management System

Backend system developed in **Python** designed using **Object-Oriented Programming (OOP)** principles, separation of responsibilities (Domain, Services, and Repositories), and persistence via **SQLAlchemy ORM**, with flexible support for **SQLite** and **Microsoft SQL Server**.

---

## 🚀 Key Features

* **Robust Domain Modeling:** Entity classes (`User`, `Expense`) protected with encapsulated properties (`@property` and `@setter`) to validate business rules at assignment time.
* **Repository Pattern:** Total decoupling between business logic and database access, facilitating testing and maintenance.
* **Services Layer (`ExpenseService`):** Centralizes business logic for creation, permission validation, and expense updates.
* **Multi-Engine Compatibility:** Configured to work with **SQLite** (ideal for local development and rapid testing) or **SQL Server** via ODBC (`pyodbc`).

---

## 📂 Project Structure

```text
Travel Expenses/
│
├── db/
│   ├── connection.py       # SQLAlchemy engine config, session, and init_db()
│   └── models.py           # ORM models (UserModel, ExpenseModel) for the database
│
├── venv/                   # Python virtual environment
├── main.py                 # Main execution and initialization script
└── README.md               # Project documentation
```

---

## 🛠️ Requirements & Installation

### 1. Prerequisites
* Python 3.10 or higher installed on your system.
* (Optional) Microsoft SQL Server and the **ODBC Driver 17 for SQL Server** if you choose to use SQL Server instead of SQLite.

### 2. Local Environment Setup
Open your terminal in the project folder and run the following commands to create and activate the virtual environment:

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment (Windows CMD / PowerShell)
venv\Scripts\activate

# Activate the virtual environment (macOS / Linux)
# source venv/bin/activate
```

### 3. Install Dependencies
Install SQLAlchemy and the ODBC driver for relational databases:

```bash
pip install sqlalchemy pyodbc
```

---

## ⚙️ Database Configuration

In the **`db/connection.py`** file, you can switch the connection string (`DATABASE_URL`) depending on the engine you want to use:

### Option A: SQLite (Default for rapid development)
Requires no additional server installation:
```python
DATABASE_URL = "sqlite:///app_gastos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
```

### Option B: Microsoft SQL Server (Windows Authentication)
Make sure you have pre-created the database on your server (e.g., `CREATE DATABASE TravelExpenses;`):
```python
DATABASE_URL = "mssql+pyodbc://@localhost/TravelExpenses?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(DATABASE_URL)
```

---

## ▶️ Running the Project

To initialize the database (automatically create user and expense tables) and run the application, execute:

```bash
python main.py
```
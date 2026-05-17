Your README is already very strong for a first real project.
Now that you’ve added:

* update quantity,
* delete item,
* CSV persistence,
* automatic loading/saving,

your README should reflect that evolution.

Here’s an updated version:

````markdown
# Restaurant Inventory Tracker

A command-line Python application for managing restaurant inventory.
Built as part of my transition from learning Python syntax to building real software projects.

---

# Features

✅ Add new inventory items  
✅ View all inventory items  
✅ Update quantity of existing inventory items  
✅ Delete inventory items  
✅ Input validation for user entries  
✅ CSV file persistence  
✅ Automatically load inventory data on startup  
✅ Automatically save inventory data before program exit  
✅ Clean command-line inventory display  
✅ Modular project structure using multiple Python files  

---

# Inventory Item Structure

Each inventory item contains:

- Item Name
- Quantity
- Unit
- Reorder Level

Example:

```text
Rice
Quantity: 50
Unit: kg
Reorder Level: 10
````

---

# Project Structure

```text
restaurant-inventory-tracker/
│
├── src/
│   ├── __init__.py
│   ├── inventory.py
│   ├── user_input.py
│   ├── views.py
│   ├── utils.py
│   └── storage.py
│
├── inventory.csv
├── main.py
├── README.md
├── .gitignore
```

---

# Application Lifecycle Architecture

This project follows a simple application lifecycle structure:

## 1. Initialization Phase

* Checks whether the CSV file exists
* Loads inventory data into memory on startup

## 2. Runtime Operations Phase

The application performs CRUD operations in memory:

* Create inventory items
* Read inventory items
* Update quantities
* Delete inventory items

## 3. Persistence Phase

Before the application exits:

* Current inventory state is saved back into the CSV file

---

# What I’m Learning Through This Project

This project is helping me practice:

* Python functions
* Lists and dictionaries
* File handling
* CSV reading and writing
* Data persistence
* State management
* Program flow design
* Input validation
* Modular project architecture
* Debugging
* Error handling
* Command-line application structure

---

# Challenges Faced During Development

## 1. Only the Last Inventory Item Was Displaying

### Cause

I mistakenly used a loop inside the inventory input function while also using a loop in `main.py`.

### Fix

Separated responsibilities properly:

* `main.py` handles application flow
* input function handles collecting one inventory item at a time

---

## 2. Dictionary Access vs Dot Notation

### Cause

I tried accessing dictionary values using dot notation:

```python
item.quantity
```

instead of:

```python
item["quantity"]
```

### Fix

Learned the difference between dictionaries and class objects in Python.

---

## 3. Understanding Application State and Persistence

### Challenge

I needed to understand how inventory data survives after the application closes.

### Solution

Implemented CSV persistence using:

* `load_from_csv()`
* `save_to_csv()`

and designed the application around:

* initialization,
* runtime state management,
* persistence lifecycle phases.

---

# Planned Features

* Low stock alerts
* Better inventory formatting
* Search functionality
* Inventory IDs
* SQLite database integration
* Unit tests

---

# Tech Stack

* Python
* CSV
* Command Line Interface (CLI)

---

# Status

🚧 Currently in active development.

This project is part of my hands-on software engineering learning journey.

```
```
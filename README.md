# Restaurant Inventory Tracker

A command-line Python application for managing restaurant inventory.
Built as part of my transition from learning Python syntax to building real software projects.

## Current Features (MVP)

* Add new inventory items
* View all inventory items
* Input validation for user entries
* Clean command-line inventory display
* Modular project structure using multiple Python files

## Inventory Item Structure

Each inventory item contains:

* Item Name
* Quantity
* Unit
* Reorder Level

Example:


Rice
Quantity: 50
Unit: kg
Reorder Level: 10


---

# Project Structure


restaurant-inventory-tracker/
│
├── src/
│   ├── __init__.py
│   ├── inventory.py
│   ├── user_input.py
│   └── utils.py
│   └── views.py
│
├── main.py
├── README.md
├── .gitignore


---

# What I’m Learning Through This Project

This project is helping me practice:

* Python functions
* Lists and dictionaries
* Program flow design
* Input validation
* Modular project architecture
* Debugging
* Error handling
* Command-line application structure

---

# Challenges Faced During Development

## 1. Only the Last Inventory Item Was Displaying

Cause:
I mistakenly used a loop inside the inventory input function while also using a loop in `main.py`.

Fix:
Separated responsibilities properly:

* `main.py` handles application flow
* input function handles collecting one inventory item at a time

---

## 2. Dictionary Access vs Dot Notation

Cause:
I tried accessing dictionary values using dot notation:

```python
item.quantity
```

instead of:

```python
item["quantity"]
```

Fix:
Learned the difference between dictionaries and class objects in Python.

---

# Planned Features

* Update inventory quantities
* Delete inventory items
* Low stock alerts
* CSV file persistence
* Load inventory automatically on startup
* Better inventory formatting
* Search functionality

---

# Tech Stack

* Python
* Command Line Interface (CLI)

---

# Status

🚧 Currently in active development.

This project is part of my hands-on software engineering learning journey.

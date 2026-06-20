# SDC43518PA

Redis CRUD User Manager

This Python program demonstrates basic CRUD operations using a Redis database. It provides a simple menu that allows you to create, read, update, and delete user records stored as Redis hashes. It was created for Performance Assessment 1.8 by Kendall Owens.

Features

Create User: add a new user with name and age

Read User: retrieve a user by ID

Update User: change a user’s name or age

Delete User: remove a single user

Delete All Data: flush the entire Redis database with confirmation

Menu-driven interface for easy navigation

Requirements

Python 3

Redis server running on 127.0.0.1:6379

Install dependency using: pip install redis

How to Run

Start your Redis server

Run the script using: python main.py

You will see a menu with options to manage users.

Data Structure
Users are stored as Redis hashes using the pattern:
user:<id>
with fields:
name
age

User IDs are generated using the Redis key:
user:id

Author
Kendall Owens
Performance Assessment 1.8

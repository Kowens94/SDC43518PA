import json

import redis

#Kendall Owens Performance Assessment 1.8
# This program demonstrates knowledge of CRUD features in databases using python
# redis server is started then user sees menu
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

r.hset("user:1", mapping={"name": "Kendall", "age": 31})
r.hset("user:2", mapping={"name": "Maine", "age": 25})
r.hset("user:3", mapping={"name": "Jack", "age": 34})
r.hset("user:4", mapping={"name": "Kiki", "age": 31})

def create_user():
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    user_id = r.incr("user:id")

    r.hset(f"user:{user_id}", mapping = {"name": name, "age": age})

    print(f"User {user_id} added!")

def read_user():
    user_id= input("Enter user ID: ")

    user = r.hgetall(f"user:{user_id}")

    if user:
        for k, v in user.items():
            print(k.decode(), ":", v.decode())

    else:
        print("User not found.")

def update_user():
    user_id = input("Enter user ID: ")

    field = input("What do you want to update? (name/age): ")
    value = input("Enter new value: ")

    r.hset(f"user:{user_id}", field, value)

    print("user updated.")

def delete_user():
    user_id = input("Enter user ID: ")

    r.delete(f"user:{user_id}")

    print("user deleted.")

def delete_all():
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ")

    if confirm.lower() == "yes":
        r.flushdb()
        print("All data deleted.")
    else:
        print("Canceled")

def main():
    while True:
        print("\---MENU---")
        print("1. Create User")
        print("2. Read/Query User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Delete Database")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_user()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            delete_all()
        elif choice == "6":
            break

main()

# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Olu Lamodi
# Assignment Number: Assignment 5
# Due Date: 07/17/2026
# Purpose: This program reads a text file containing day of week and temperature
# readings, stores all of that data into a SQLite database, then runs SQL
# queries to compute and print the average temperature for Sunday and Thursday.
# Resources used: Python sqlite3 docs (docs.python.org), class notes on databases.

import sqlite3
import os

# delete the database file if it already exists so we start fresh every run
# otherwise we would get duplicate entries if we ran the program more than once
if os.path.exists("temperatures.db"):
    os.remove("temperatures.db")

# create the database and connect to it
conn = sqlite3.connect("temperatures.db")
cursor = conn.cursor()

# create the table with the fields from the assignment
cursor.execute("""
    CREATE TABLE temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# read the input file and insert each row into the table
with open("Assignment5input.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        # skip blank lines just in case
        if len(parts) == 2:
            day = parts[0]
            temp = float(parts[1])
            cursor.execute("INSERT INTO temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)", (day, temp))

# save the inserts to the database
conn.commit()

print("Database created and data inserted successfully.")
print()

# run a SQL query to get the average temperature for Sunday
cursor.execute("SELECT AVG(Temperature_Value) FROM temperatures WHERE Day_Of_Week = 'Sunday'")
sunday_avg = cursor.fetchone()[0]
print(f"Average temperature for Sunday: {sunday_avg:.4f}")

# run a SQL query to get the average temperature for Thursday
cursor.execute("SELECT AVG(Temperature_Value) FROM temperatures WHERE Day_Of_Week = 'Thursday'")
thursday_avg = cursor.fetchone()[0]
print(f"Average temperature for Thursday: {thursday_avg:.4f}")

# close the connection when done
conn.close()
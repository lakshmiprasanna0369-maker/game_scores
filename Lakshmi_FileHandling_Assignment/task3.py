# Task 3: Append New Student and Create Log
# Append new student to existing file
with open("students.txt", "a") as file:
    file.write("Eve, 88\n")
# Create activity log file
with open("activity.log", "w") as log:
    log.write("Added new student: Eve")
print("New student added and activity logged successfully")
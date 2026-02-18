# Task 2: Read and Display Data
try:
    with open("students.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            print(f"Student: {name.strip()}, Score: {score.strip()}")

except FileNotFoundError:
    print("Error: students.txt file not found")
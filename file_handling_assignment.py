# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("This is line 3 with some special characters like !@#$%\n")
except Exception as e:
    print("An error occurred while creating the file:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to read the file.")
except Exception as e:
    print("An error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 added in append mode.\n")
        file.write("Appending another line, line 5.\n")
        file.write("The last line, line 6.\n")
except Exception as e:
    print("An error occurred while appending to the file:", e)

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File handling completed.")

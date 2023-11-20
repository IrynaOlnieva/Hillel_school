# Create a file with numbers (in a few rows)
# Read this file, and print the sum of all numbers (create a new function for it)
# Use try\except block to avoid other symbols except numbers in the file

def sum_of_numbers():
    try:
        numbers_file = open("text_1.txt", "r")
    except Exception:
        print("There was an error opening the file")
    else:
        total = 0
        for line in numbers_file:
            try:
                number = int(line)
                total += number
            except ValueError:
                print(f"Skipping non-numeric line: {line}")
        print("Sum of numbers:", total)
        numbers_file.close()

sum_of_numbers()

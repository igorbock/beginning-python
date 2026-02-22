# Starter inputs
numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

# Task 1: Sort numbers in ascending order
# Task 2: Sort numbers in descending order
# Task 3: Sort words alphabetically
# Task 4: Sort words by length

# Replace 'pass' with your code for each task
ascending_numbers = sorted(numbers)
descending_numbers = sorted(numbers, reverse=True)
alphabetical_words = sorted(words)
length_sorted_words = sorted(words, key=len)

# Print the results
print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)
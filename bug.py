def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Example usage
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
print(f"The average of an empty list is: {calculate_average(my_empty_list)}")

# The following will throw an exception
my_string_list = [1, 2, "a", 4, 5]
#average = calculate_average(my_string_list)
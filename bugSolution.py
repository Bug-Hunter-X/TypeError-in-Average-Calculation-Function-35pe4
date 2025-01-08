def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

#Example usage
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
print(f"The average of an empty list is: {calculate_average(my_empty_list)}")

my_string_list = [1, 2, "a", 4, 5]
average = calculate_average(my_string_list)
print(f"The average is: {average}")

my_mixed_list = [1,2, 3.14, 4, 5]
average = calculate_average(my_mixed_list)
print(f"The average is: {average}")

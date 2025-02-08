def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list) # This will correctly return 0
print(f"The average of an empty list is: {average}")

my_list = [10,20,'a',40,50]
average = calculate_average(my_list) # This will now correctly return the average of numeric values only
print(f"The average is: {average}") 
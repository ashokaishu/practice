def find_smallest_largest(numbers):
    if not numbers:
        return None, None  # Return None for both smallest and largest if the list is empty

    smallest = largest = numbers[0]  # Initialize smallest and largest with the first number

    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

numbers = [50, 1002, 398, 876, 150, 246]
smallest, largest = find_smallest_largest(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)




def calculate_sum(numbers):
    """Calculate sum using a loop (cannot use built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculate average using the sum function above."""
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)


def calculate_maximum(numbers):
    """Find maximum value using a loop (cannot use built-in max())."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def calculate_minimum(numbers):
    """Find minimum value using a loop (cannot use built-in min())."""
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val



if __name__ == "__main__":
    n = int(input("How many numbers? "))
    
    # Requirement: N must be positive
    if n <= 0:
        print("Error: Number of values must be positive.")
    else:
        numbers = []
        

        for i in range(1, n + 1):
            num = int(input(f"Enter number {i}: "))
            numbers.append(num)
        
        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers):.1f}")
        print(f"Maximum: {calculate_maximum(numbers)}")
        print(f"Minimum: {calculate_minimum(numbers)}")
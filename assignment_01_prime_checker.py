

def is_prime(number):
    """Check if a number is prime."""
    
    # Numbers less than 2 are NOT prime
    if number < 2:
        return False
    
    # 2 is prime
    if number == 2:
        return True
    
    # Even numbers (except 2) are NOT prime
    if number % 2 == 0:
        return False
    
    # Check for odd divisors from 3 to square root of number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True


# Main program
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")
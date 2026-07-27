
def single_table(number):
    """
    PART A: Print the multiplication table for a single number (1 to 12).
    """
    if number <= 0:
        print("Error: Number must be a positive integer.")
        return
    
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2}  =  {number * i}")


def tables_up_to_n(n):
    """
    PART B: Print multiplication tables for every number from 1 to N.
    """
    if n <= 0:
        print("Error: Number must be a positive integer.")
        return
    
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num}  x  {i:<2}  =  {num * i}")

        if num < n:
            print("---------------------------")



if __name__ == "__main__":
    print("=== MULTIPLICATION TABLE GENERATOR ===\n")

    
    print("PART A — Single Table")
    num = int(input("Enter a number:5"))

    if num <= 0:
        print("Error: Number must be a positive integer.")
    else:
        single_table(num)

    
    print("\n" + "=" * 50)
    print("PART B — Tables from 1 to N")
    n = int(input("Enter a number N:3"))
    
    if n <= 0:
        print("Error: Number must be a positive integer.")
    else:
        tables_up_to_n(n)
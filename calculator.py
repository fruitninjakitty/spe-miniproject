def calculate_square_root(number):
    """
    Computes the square root of a non-negative number.
    
    Args:
        number: Input value (must be ≥ 0)
    
    Returns:
        Square root value or error message
    """
    if number < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return number ** 0.5

def compute_factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        n: Input integer (must be ≥ 0)
    
    Returns:
        Factorial value or error message
    """
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is not defined for negative numbers or non-integers."
    
    result = 1
    for current in range(1, n + 1):
        result *= current
    return result

def approximate_natural_log(number):
    """
    Approximates the natural logarithm using limit definition.
    
    Args:
        number: Input value (must be > 0)
    
    Returns:
        Approximate ln(value) or error message
    """
    if number <= 0:
        return "Error: Natural logarithm requires positive numbers."
    iterations = 1000.0  # Higher iterations improve accuracy
    return iterations * (number ** (1/iterations) - 1)

def exponentiate(base, power):
    """
    Computes base raised to an integer power using iterative multiplication.
    
    Args:
        base: Number to be exponentiated
        power: Integer exponent
    
    Returns:
        Result of base^power calculation
    """
    result = 1
    for _ in range(int(abs(power))):
        result *= base
    return 1 / result if power < 0 else result

def calculator_shell():
    """
    Command-line interface for mathematical operations
    """
    print("Scientific Calculator\n" + "-"*23)
    
    while True:
        print("\nOperations:")
        print("1. Square Root\n2. Factorial\n3. Natural Log\n4. Power\n5. Exit")
        
        try:
            choice = input("Enter choice (1-5): ")
            
            if choice == '5':
                print("Exiting calculator...")
                break

            if choice not in ('1','2','3','4'):
                print("Invalid choice! Please select 1-5")
                continue

            # Common input handling
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid number format!")
                continue

            if choice == '1':
                result = calculate_square_root(num)
            elif choice == '2':
                result = compute_factorial(int(num))
            elif choice == '3':
                result = approximate_natural_log(num)
            elif choice == '4':
                try:
                    exponent = float(input("Enter exponent: "))
                except ValueError:
                    print("Invalid exponent format!")
                    continue
                result = exponentiate(num, exponent)

            # Handle error messages and results
            if isinstance(result, str) and result.startswith("Error"):
                print(result)
            else:
                print(f"Result: {result:.6f}")  # Format to 6 decimal places

        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break

if __name__ == "__main__":
    calculator_shell()
    #just testing the webhooks




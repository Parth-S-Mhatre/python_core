def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def calculate_factorial(n):
    """Calculate factorial of a number using a while loop."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    count = 1
    while count <= n:
        factorial *= count
        count += 1
    return factorial

# Example usage
if __name__ == "__main__":
    # Temperature Conversion
    temp_celsius = 25
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C is equal to {temp_fahrenheit:.2f}°F")

    temp_fahrenheit = 77
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit}°F is equal to {temp_celsius:.2f}°C")

    # Factorial Calculation
    number = 5
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is {factorial_result}")
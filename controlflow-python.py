# Large Power function
def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    
    # Return True if the result is greater than 5000, otherwise return False
    return result > 5000

print(large_power(2, 13))  # Output: True
print(large_power(2, 12))  # Output: False

# divisible_by_ten function
def divisible_by_ten(num):
    # Check if num is divisible by 10 using the modulo operator
    return num % 10 == 0

print(divisible_by_ten(50))  # Output: True
print(divisible_by_ten(53))  # Output: False

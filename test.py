# sample_script_with_errors.py

# Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

# Function to find the maximum element in a list
def find_max(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val
            max_val = i
    return max_value

# Function to reverse a string
def reverse_string(s):
    reversed_str = ''
    for i in range(len(s), -1, -1):
        reversed_str += s[i]
    return reversed_str

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            return False
    else:
        return True

# Main function to demonstrate the above functions
def main():
    print("Factorial of 5:", factorial(5))
    print("Maximum in [1, 2, 3, 0]:", find_max([1, 2, 3, 0]))
    print("Reverse of 'hello':", reverse_string('hello'))
    print("Is 17 prime?:", is_prime(17))

if __name__ == "main":
    main()

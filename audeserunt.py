# Define a function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main program to calculate and print factorial of 5
def main():
    num = 5
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

# Run the main function
if __name__ == "__main__":
    main()

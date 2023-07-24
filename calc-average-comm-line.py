# Simple Calculate Average Tool

def calculate_average(numbers):
    # Calculate the sum of all numbers in the list
    total = sum(numbers)
    # Calculate the average by dividing the total by the number of elements in the list
    return total / len(numbers)


def main():
    # Print a welcome message
    print("Welcome to the Average Calculator!")
    # Prompt the user to enter a list of numbers separated by spaces
    print("Enter a list of numbers separated by spaces:")

    try:
        # Read the user input as a string and split it into individual numbers using spaces as separators
        input_numbers = input().split()
        numbers = [float(num) for num in input_numbers]
        average = calculate_average(numbers)
        print(f"The average of the numbers is: {average:.2f}")

    except ValueError:
        # If the user enters invalid input (e.g., non-numeric values), handle the exception
        print("Invalid input. Please enter a list of valid numbers separated by spaces.")


if __name__ == "__main__":
    # Call the main function to start the average calculator
    main()
    
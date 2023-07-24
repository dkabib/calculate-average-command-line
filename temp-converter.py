# Temp converter tool

def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9
    return (fahrenheit - 32) * 5/9


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
    
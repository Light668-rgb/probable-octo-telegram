def check_number(number):
    if number == 0:
        print("The entered number is zero.")
    elif number % 2 == 0:
        print("The entered number is even.")
    else:
        print("The entered number is odd.")

def main():
    try:
        user_input = int(input("Enter a number: "))
        check_number(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
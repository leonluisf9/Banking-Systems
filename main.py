"""This function handles the transfer process for the user."""
# TODO: Import the Checking, Savings, and Validation classes
# TODO: These should be imported from the appropriate file in the BankingClasses directory.
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation
# TODO: Import the handle_deposit, handle_withdrawal, handle_transfer, and balances functions
# TODO: These should be imported from the appropriate file in the BankingFunctions directory.
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.withdraw import handle_withdrawal
from BankingFunctions.transfer import handle_transfer, balances

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
           "contain at least one uppercase and lowercase letter,\n"
           "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # TODO: Initialize the attempts variable to 1.
    attempts = 1
    # TODO: Create a while loop to validate the email and password.
    # TODO: The while loop should run as long as the attempts variable is less than 3.
    while attempts < 3:
        # TODO: Validate the email and password using the Validation class.
        validated_email = Validation.validate_email(email)
        validated_password = Validation.validate_password(password)
        if validated_email == False or validated_password == False: 
            # If the email and password are invalid,
            # print a message and prompt the user to enter their email and password again.
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1
        # TODO: Otherwise, break out of the loop.
        else:
            break
    # TODO: If the maximum number of attempts is reached, print a message and exit the program.
    if attempts == 3:
        print("Maximum number of attempts reached. Exiting program.")
        return

    # Set up accounts with default balances.
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # Print a message for the user inform them of their checking and savings balances
    print("Here are your account balances:")
    # TODO: Use the get_balance method to retrieve the current balance of each account.
    print(f"Checking: ${checking_account.get_balance():,.2f}")
    print(f"Savings: ${savings_account.get_balance():,.2f}")
    # TODO: Write while loop to present options for the user.
    # TODO: Present a menu of options to the user.
    # TODO: Allowing them to make deposits, withdrawals, or transfers between accounts.
    while True:
        # TODO: Create a list of valid choices.
        print("\nWhat would you like to do?")
        print("Make a deposit? Enter 1")
        print("Make a withdrawal? Enter 2")
        print("Make a transfer? Enter 3")
        print("Check account balances? Enter 4")
        print("Quit? Enter q\n")
        choice = input("Enter your choice:")
            # TODO: Use if/elif conditional statements to check the user's choice.
        choice = choice.upper()
        if choice == 'Q':
            break
            # TODO: If the choice is in the list of valid choices, call the appropriate function.
            # TODO: Pass in the checking_account and savings_account objects.
        elif choice == '1':
            handle_deposit(checking_account, savings_account)
        elif choice == '2':
            handle_withdrawal(checking_account, savings_account)
        elif choice == '3':
            handle_transfer(checking_account, savings_account)
        elif choice == '4':
            balances(checking_account, savings_account)   
        # TODO: If the user enters an invalid choice, print a message.
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or q.\n")

if __name__ == "__main__":
    main()

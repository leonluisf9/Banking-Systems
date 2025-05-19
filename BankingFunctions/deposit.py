"""This function handles the deposit process for the user."""
# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.
def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    # TODO: Prompt the user to select an account and make a deposit.
    account_choice = input("Enter 1 for checking,\n"
                           "enter 2 for savings,\n"
                           "enter q to quit: ") 
    # TODO: If the user chooses to quit, return from the function.
    if account_choice == 'q':
        return
    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if account_choice in ['1', '2']:
            try:
                # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                amount = float(input("Enter the amount to deposit: "))
            # Use the ValueError as an exception.
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.
                print("Please enter a dollar amount.\n")
                # TODO: Call the handle_deposit function recursively for an invalid amount.
                handle_deposit(checking, savings)
                # TODO: Ensure the function returns after the recursive call.
                return
            # TODO: Add an if/else conditional statement to check the account choice,
            if account_choice == '1':
                # TODO: Call the withdraw method on the appropriate account.
                print(f"Depositing ${amount:,.2f} into checking.")
                checking.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
                checking = checking.get_balance()
                print("New Balance:")
                print(f"Checking: ${checking:,.2f}")               
            else:
                # TODO: Call the deposit methods on the appropriate account.
                print(f"Depositing ${amount:,.2f} into savings.")
                savings.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
                savings = savings.get_balance()
                print("New Balance:")
                print(f"Savings: ${savings:,.2f}")
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")      
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)

"""
File: AleynaPham_ProgrammingExercise_3.py
Description: Program prompts user for monthly expenses (type & amount), uses
reduce method to analyze the data, then displays total expense, lowest expense,
and highest expense.
"""

from functools import reduce

def get_expenses():
    """
    Prompts user to type their monthly expenses (type & amount).

    Parameters:
        None

    Variables:
        expense_list (list): Records dictionary entries of expenses.
        continue_input (str): Controls input loop.
        expense_type (str): Name of expense.
        amount_input (str): Raw user input for cost.
        expense_amount (float): Numerical value of expense.

    Logic:
        1. Create empty list (expense_list).
        2. Begin while loop prompting user for monthly expenses.
        3. Receive expense name and amount from user.
        4. If expense name is empty, break out of loop.
        5. Convert amount to float and add dictionary to list.
        6. Prompt user if they wish to add another expense.
        7. Return expense_list.

    Return:
        list: List of expense dictionaries that contain 'type' and 'amount'.
    """
    # Create empty list to store all expenses entered by user.
    expense_list = []

    # Loop control variable.
    continue_input = "yes"

    print("──────────────────────────────────────────")
    print("  ⋆✴︎˚｡⋆ Monthly Expense Analysis ⋆✴︎˚｡⋆")
    print("──────────────────────────────────────────")

    # Continue prompting user for expenses until user enters 'no.'
    while continue_input.lower() == "yes":
        # Receive name of expense.
        expense_type = input("\nWhat type of expense is this? ")

        # If left blank, exit loop.
        if expense_type == "":
            break

        # Receive value of expense.
        amount_input = input("\nHow much does " + expense_type + " cost? $")

        # Convert user input string to float number.
        expense_amount = float(amount_input)

        # Record expense in dictionary.
        expense_list.append({"type": expense_type, "amount": expense_amount})

        # Question user if they wish to continue their list of expenses.
        continue_input = input("\nWould you like to add another expense? (yes/no): ")

    # Return total list of expenses.
    return expense_list

def analyze_expenses(expenses):
    """
    Calculates total, lowest, and highest expenses using reduce method.

    Parameters:
        expenses (list): List of expense dictionaries.

    Variables:
        total_amount (float): Total expense amount.
        highest_expense (dict): Expense dictionary with maximum amount.
        lowest_expense (dict): Expense dictionary with minimum amount.

    Logic:
        1. Use reduce method with lambda to calculate total expense.
        2. Use reduce method with lambda to locate dictionary with maximum amount.
        3. Use reduce method with lambda to locate dictionary with minimum amount.
        4. Return total_amount, highest_expense, and lowest_expense.

     Return:
        tuple: total_amount, highest_expense, and lowest_expense.
    """
    # Use reduce method with lambda to calculate total expense.
    total_amount = reduce(lambda acc, item: acc + item["amount"], expenses, 0.0)

    # Use reduce method with lambda to locate dictionary with maximum amount.
    highest_expense = reduce(
        lambda current, item: item if item["amount"] > current["amount"] else current,
        expenses
    )

    # Use reduce method with lambda to locate dictionary with minimum amount.
    lowest_expense = reduce(
        lambda current, item: item if item["amount"] < current["amount"] else current,
        expenses
    )

    # Return calculations.
    return total_amount, highest_expense, lowest_expense

def main():
    """
    Main function operating input, calculations, and output.

    Parameters:
        None

    Variables:
        user_expenses (list): Returned expense list retrieved from get_expenses.
        total (float): Total expense amount retrieved from analyze_expenses.
        highest (dict): Dictionary of maximum expense.
        lowest (dict): Dictionary of minimum expense.

    Logic:
        1. Call get_expenses to compile expenses entered by user.
        2. Print error message if list is left empty.
        3. Call analyze_expenses to calculate statistics.
        4. Print total expense amount, highest expense cost and its label,
           and lowest expense cost and its label.

    Return:
        None
    """
    # Receive user expenses.
    user_expenses = get_expenses()

    # Verify if user left list empty.
    if len(user_expenses) == 0:
        print("\nNo expenses were found... Please enter something!")
    else:
        # Calculate statistics using analyze_expenses function.
        total, highest, lowest = analyze_expenses(user_expenses)

        # Print results.
        print("\n⋆˙⟡ Your results are ready! ⋆˙⟡")
        print("\nTotal Expenses: $" + str(total))
        print("Highest Expense: " + highest["type"] + " ($" + str(highest["amount"]) + ")")
        print("Lowest Expense: " + lowest["type"] + " ($" + str(lowest["amount"]) + ")")

# Run main function.
if __name__ == "__main__":
    main()


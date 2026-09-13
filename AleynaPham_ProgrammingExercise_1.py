"""
File: AleynaPham_ProgrammingExercise_1.py
Description: Pre-sale program that manages a limited number of cinema tickets.
"""

TOTAL_TICKETS = 10
MAX_PER_BUYER = 4

# Function 1: Check if transaction meets purchase conditions
# and revise ticket count.
def check_transaction(desired_tickets, remaining_tickets):
    """
    Authenticates requested tickets before updating inventory.

    Parameters:
        desired_tickets (int): Number of tickets requested by buyer.
        remaining_tickets (int): Number of tickets remaining.

    Variables:
        desired_tickets (int): Value fed into function that represents request.
        remaining_tickets (int): Value refreshed and returned by function.

    Logic:
        1. Verify if buyer requires value outside 1-4 range.
        2. Verify if buyer's value exceeds remaining tickets.
        3. Complete transaction, refresh remaining tickets, then return value.

    Return:
        int: Updated remaining ticket value.
    """
    # Check if buyer requires value outside 1-4.
    if desired_tickets < 1 or desired_tickets > MAX_PER_BUYER:
        print('Please enter a number between 1 and 4.')
        return remaining_tickets

    # Check if buyer requires a value exceeding the remaining value.
    elif desired_tickets > remaining_tickets:
        print('Error. Number exceeds remaining tickets.')
        return remaining_tickets

    # Finish transaction and update remaining tickets.
    else:
        remaining_tickets = remaining_tickets - desired_tickets
        print('Transaction completed.')
        print('Remaining tickets: ' + str(remaining_tickets))
        return remaining_tickets

# Function 2: Run main program loop and set up starting values.
def main():
    """
    Runs main program loop and tracks total buyers.

    Parameters:
        None

    Variables:
        total_tickets (int): Counter tracking unsold tickets from value 20.
        total_buyers (int): Accumulator counting buyers who made transactions.
        user_input (int): Ticket count requested by buyer.
        new_total_tickets (int): Returned value from check_transaction() function.

    Logic:
        1. Set up ticket count to 20 and total buyers to 0.
        2. Continuously loop if tickets exceed 0.
        3. Prompt buyer for desired value and run validation function.
        4. Add to total_buyers accumulator if transaction is completed.
        5. Print a final message when ticket value reaches 0.

    Return:
        None
    """
    # Establishes starting inventory tracker using a constant value.
    total_tickets = TOTAL_TICKETS

    # Establishes starting buyer accumulator.
    total_buyers = 0

    # Store operates until number of tickets reaches zero.
    while total_tickets > 0:
        print('\nTickets available: ' + str(total_tickets))
        user_input = int(input('How many tickets do you wish to purchase? '))

        # Check new count through check_transaction function.
        new_total_tickets = check_transaction(user_input, total_tickets)

        # If ticket value decreased, increase buyer count by 1.
        if new_total_tickets < total_tickets:
            total_tickets = new_total_tickets
            total_buyers = total_buyers + 1

    # Display final total after loop concludes.
    print('\nTickets have been sold out.')
    print('Total buyers: ' + str(total_buyers))

# Start program.
if __name__ == '__main__':
    main()

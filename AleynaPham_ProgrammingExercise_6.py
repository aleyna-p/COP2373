"""
File: AleynaPham_ProgrammingExercise_6.py
Description: Program prompts user for a phone number, social security number,
zip code, validates each input using regular expressions, then displays
whether each entry is valid or invalid.
"""

import re

def validate_phone(phone_number):
    """
    Validates the phone number using a regular expression.

    Parameters:
        phone_number (str): Raw string input for phone number.

    Variables:
        pattern (str): Regular expression pattern for XXX-XXX-XXXX mobile format.

    Logic:
        1. Define regex pattern to match digit format.
        2. Confirm if phone_number matches pattern.
        3. Return True if valid, False if invalid.

    Return:
        bool: True if phone number is valid, False if invalid.
    """
    # Define regex pattern for phone number.
    pattern = r"^\d{3}-\d{3}-\d{4}$"

    # Confirm if user input matches regular expression pattern.
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def validate_ssn(ssn_number):
    """
    Validates the standard Social Security Number using a regular expression.

    Parameters:
        ssn_number (str): Raw string input for social security number.

    Variables:
        pattern (str): Regular expression pattern for XXX-XX-XXXX SSN format.

    Logic:
        1. Define regex pattern to match SSN format.
        2. Check if ssn_number matches pattern.
        3. Return True if valid, False if invalid.

    Return:
        bool: True if SSN is valid, False if invalid.
    """
    # Define regex pattern for SSN.
    pattern = r"^\d{3}-\d{2}-\d{4}$"

    # Confirm if user input matches regular expression pattern.
    if re.match(pattern, ssn_number):
        return True
    else:
        return False


def validate_zip(zip_code):
    """
    Validates the zip code using a regular expression.

    Parameters:
        zip_code (str): Raw string input for zip code.

    Variables:
        pattern (str): Regular expression pattern for XXXXX or XXXXX-XXXX zip format.

    Logic:
        1. Define regex pattern to match zip code format.
        2. Check if zip_code matches pattern.
        3. Return True if valid, False if invalid.

    Return:
        bool: True if zip code is valid, False if invalid.
    """
    # Define regex pattern for zip code.
    pattern = r"^\d{5}(-\d{4})?$"

    # Confirm if user input matches regular expression pattern.
    if re.match(pattern, zip_code):
        return True
    else:
        return False


def main():
    """
    Main function operating input collection, validation, and output display.

    Parameters:
        None

    Variables:
        phone_input (str): User input for phone number.
        ssn_input (str): User input for social security number.
        zip_input (str): User input for zip code.

    Logic:
        1. Print header for data validation program.
        2. Prompt user to enter phone number, SSN, and zip code.
        3. Call validation functions for each input.
        4. Print results displaying validity of each entry.

    Return:
        None
    """
    print("\n═══════✿═══════╡°˖✧✿✧˖°╞═══════✿═══════")
    print("   Phone Number, SSN, Zip Code Checker ")
    print("═══════✿═══════╡°˖✧✿✧˖°╞═══════✿═══════")

    # Prompt user for data inputs.
    phone_input = input("\nPlease enter a phone number (XXX-XXX-XXXX): ")
    ssn_input = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_input = input("Enter a zip code (XXXXX or XXXXX-XXXX): ")

    print("\n⋆˚✿˖° Your results are ready! °˖✿˚⋆")

    # Validate then display results for phone number.
    if validate_phone(phone_input):
        print("\nPhone Number (" + phone_input + "): VALID")
    else:
        print("\nPhone Number (" + phone_input + "): INVALID")

    # Validate then display results for SSN.
    if validate_ssn(ssn_input):
        print("Social Security Number (" + ssn_input + "): VALID")
    else:
        print("Social Security Number (" + ssn_input + "): INVALID")

    # Validate then display results for zip code.
    if validate_zip(zip_input):
        print("Zip Code (" + zip_input + "): VALID")
    else:
        print("Zip Code (" + zip_input + "): INVALID")


# Run main function.
if __name__ == "__main__":
    main()
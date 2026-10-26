"""
File: AleynaPham_ProgrammingExercise_7.py
Description: Program prompts user to input a paragraph, then
             separates the text into individual sentences using
             regular expressions, and finally prints each sentence
             along with total count.
"""

import re

def extract_sentences(text):
    """
    Splits paragraph text into a list of individual sentences.
    Handles sentences beginning with capital letters or numbers.
    Uses look-ahead rules so abbreviations and decimals don't break sentences.

    Parameters:
        text (str): Paragraph typed by user.

    Variables:
        pattern (str): Regular expression pattern with look-ahead rules.
        sentence_list (list): List containing all found sentences.

    Logic:
        1. Arrange regex pattern to search for sentences beginning with
           letters or numbers.
        2. Match text to a period, question mark, or exclamation point.
        3. Use look-ahead to prevent splitting on abbreviations or decimals.
        4. Use re.findall with DOTALL and MULTILINE flags to grab everything.
        5. Return list of sentences.

    Return:
        list: A list of sentences found in the text.
    """
    # Pattern matches sentences beginning with capital letter or number [A-Z0-9],
    # stops at punctuation [.!?], and uses look-ahead (?= [A-Z0-9]|$).
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Find each sentence in text using pattern and required flags.
    sentence_list = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)

    return sentence_list


def main():
    """
    Main function running program, retrieves user input, calls
    extraction function, then prints results.

    Parameters:
        None

    Variables:
        user_paragraph (str): Text entered by user.
        sentences (list): List of sentences returned by function.
        count (int): Total number of sentences found.

    Logic:
        1. Print header for program.
        2. Prompt user for paragraph.
        3. Call extract_sentences function.
        4. Count number of sentences found.
        5. Print each sentence on new line with arrow.
        6. Print total sentence count.

    Return:
        None
    """
    print("──────────────────────────────────────────")
    print("      ⋆✴︎˚｡⋆ Sentence Analyzer ⋆✴︎˚｡⋆")
    print("──────────────────────────────────────────")

    # Prompt user for paragraph.
    user_paragraph = input("\nPlease enter a paragraph:\n")

    # Call function to receive sentences.
    sentences = extract_sentences(user_paragraph)

    # Count number of sentences.
    count = len(sentences)

    print("\nજ⁀➴ Results ⋆˚✿˖° ")

    # Loop through and print each sentence.
    for sentence in sentences:
        print("\n-> " + sentence)

    # Print total count.
    print("\nTotal sentence count: " + str(count))


# Run main function.
if __name__ == "__main__":
    main()
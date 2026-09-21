"""
File: AleynaPham_ProgrammingExercise_2.py
Description: Finds common spam keywords/phrases in text from
user-entered email messages, computes total spam score, calculates
likelihood of email message being spam based on number of points.
"""

# List of 30 common spam keywords and phrases.
SPAM_KEYWORDS = [
    "Free money", "no obligation", "pure profit", "limited time", "Act now",
    "best price", "special promotion", "refinance", "unsecured credit",
    "You've been selected", "extra cash", "no hidden costs", "no fees",
    "money back", "cash bonus", "save", "earn", "lower interest rates",
    "cashback", "Only a few left", "Hurry", "Don't miss", "Urgent", "Winner",
    "coupon", "Save big", "Attention", "Congratulations", "Download now"
]

def scan_spam(message):
    """
    Scans email message for occurrences of listed spam keywords/phrases.

    Parameters:
        message (str): Email message text entered by user.

    Variables:
        message_lower (str): Lowercase version of input email message text.
        score (int): Accumulator tracking total spam keyword/phrase matches detected.
        detected_triggers (list): List of detected spam keyword/phrase matches.

    Logic:
    1. Make message lowercase.
    2. Set score to 0 and detected_triggers to empty list.
    3. Loop through SPAM_KEYWORDS.
    4. Keep count of occurrences of spam keyword/phrase matches.
    5. If count exceeds 0, add to score and list.
    6. Return score and detected_triggers list.

    Return:
        tuple: Returns both total score and detected list.
    """
    # Convert input email message text to lowercase so scan isn't case-sensitive.
    message_lower = message.lower()

    # Initialize total score accumulator.
    score = 0

    # Initialize list that stores matching keywords/phrases.
    detected_triggers = []

    # Loop through list of 30 keywords/phrases.
    for keyword in SPAM_KEYWORDS:
        # Check number of occurrences of keyword/phrase in email message text.
        occurrences = message_lower.count(keyword.lower())

        # Refresh score and trigger list if keyword/phrase appears.
        if occurrences > 0:
            score = score + occurrences
            # Construct string displaying keyword/phrase and the number of occurrences.
            match_info = keyword + " (found " + str(occurrences) + " time(s))"
            detected_triggers.append(match_info)

    # Return total score and list of matched keywords/phrases.
    return score, detected_triggers

def receive_spam_rating(score):
    """
    Calculates spam likelihood rating based on spam score.

    Parameters:
        score (int): Total calculated spam score.

    Variables:
        None

    Logic:
        1. Use if-elif-else branching to calculate score.
        2. If score = 0, return "Not Spam".
        3. If score <= 2, return "Low Likelihood".
        4. If score <= 5, return "Moderate Likelihood".
        5. Else, return "High Likelihood".

    Return:
        str: Description of spam likelihood rating.
    """
    # Check range of score by branching.
    if score == 0:
        return "Not Spam"
    elif score <= 2:
        return "Low Likelihood"
    elif score <= 5:
        return "Moderate Likelihood"
    else:
        return "High Likelihood"

def main():
    """
    Runs main email scanning program then prints the results.

    Parameters:
        None

    Variables:
        user_email (str): Text input by user.
        score (int): Calculated score using scan_spam function.
        detected_triggers (list): Matched keywords/phrases from scan_spam function.
        rating (str): Result string using receive_spam_rating function.

    Logic:
        1. Print title.
        2. Prompt user to enter email message text.
        3. If input is empty, print error message.
        4. Else, run scan_spam and receive_spam_rating functions.
        5. Print result.

    Return:
        None
    """
    print("༺☆༻ Spam Scanner ༺☆༻")

    # Prompt user input.
    user_email = input("Please enter the email you wish to scan:\n")

    # Check if input is empty.
    if user_email == "":
        print("\nNo text found. Please enter text.")
    else:
        # Call functions to scan text.
        score, detected_triggers = scan_spam(user_email)
        rating = receive_spam_rating(score)

        # Print result.
        print("\n ── ⋆⋅☆⋅⋆ ──")
        print("Scan Complete!")
        print(" ── ⋆⋅☆⋅⋆ ──")
        print("Spam Score: " + str(score))
        print("Is this spam?: " + rating)
        print("\nFlagged Keywords/Phrases:")

        # Print matched keywords/phrases or a clean message.
        if len(detected_triggers) > 0:
            for trigger in detected_triggers:
                print(" - " + trigger)
        else:
            print(" - All clean!")

# Run main function.
if __name__ == "__main__":
    main()



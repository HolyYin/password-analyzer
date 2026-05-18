
                                                                ♰ 𝚢𝚒𝚗 ♰
README - Password Analyzer
==========================
IT IS HIGHLY RECCOMENDED TO OPEN THIS FILE WITH NOTEPAD FOR A BETTER READABILITY
==========================

This project contains a simple password analyzer written in Python.
The program asks the user to enter a password, checks it against several
security rules, and gives feedback about how strong the password is.

The code is designed to be clear and readable.


1. What the code is supposed to do
==================================

The program analyzes a password entered by the user and checks whether it meets
basic security requirements.

The program checks:

- whether the password appears in a wordlist of common passwords;
- whether the password length is between a minimum and maximum value;
- whether the password contains non-ASCII characters;
- whether the password contains repeated consecutive characters;
- whether the password contains at least one symbol;
- whether the password contains at least one number;
- whether the password contains at least one lowercase letter;
- whether the password contains at least one uppercase letter.

At the end of the analysis, the password is classified as:

- strong password, if all main requirements are met;
- medium password, if only one of the character-type requirements is missing;
- weak password, if two or more character-type requirements are missing or if
  other important problems are found.

If the password is not valid or not strong enough, the program asks the user to
enter another password.


2. Input
========

The program receives a password from the user through the input() function.

Example:

Enter your password: Password123!

The program also uses an external wordlist file.
This file contains many common passwords (100k), one password per line.

In the code, the wordlist file path is stored in the WORDLIST_PATH constant:

D:\informatica\python cod\cybersecurity related stuff\PswAnalyzer\100kmostcommon.txt

This file must exist in the specified location. If it does not exist, Python
will raise an error because it will not be able to open the file.


3. Output
=========

The program prints a message that describes the strength of the password.

Possible outputs:

Strong password!

Medium password. Suggestions: Add symbols

Weak password. Suggestions: Add numbers, Add uppercase letters

The program also stores some messages inside the log list.
These messages are not printed automatically, but they remain available inside
the program to check which problems were found.

Example of a message stored in log:

Password 'password123' found in wordlist.


4. Code explanation
===================

import string  # Imports the string module from the Python standard library. This module contains useful predefined strings, including string.punctuation, which is used to check if the password contains symbols.

log = []  # Creates an empty list called log. This list stores messages about problems found during the password analysis.

MIN_LENGTH = 8  # Defines the minimum allowed password length. In this program, the password must have at least 8 characters.
MAX_LENGTH = 32  # Defines the maximum allowed password length. In this program, the password must not be longer than 32 characters.
BASE_DIR = Path(__file__).resolve().parent      # Gets the directory where this script is located
WORDLIST_PATH = BASE_DIR / "100kmostcommon.txt" # Builds the path to the wordlist file inside that directory


def password_in_wordlist(psw):  # Defines a function that checks whether the password stored in psw appears inside the wordlist file.
    with open(WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as file:  # Opens the wordlist file in read mode. UTF-8 is used as the encoding, and unreadable characters are ignored to avoid decoding errors.
        for line in file:  # Reads the file one line at a time. This is efficient because the whole file is not loaded into memory at once.
            if psw == line.strip():  # Compares the user's password with the current line. strip() removes spaces and newline characters from the beginning and end of the line.
                return True  # Returns True immediately if the password is found in the wordlist.
    return False  # Returns False if the entire file has been checked and the password was not found.


def analyze_password():  # Defines the main function of the program. This function asks for the password, analyzes it, and prints the result.
    first_attempt = True  # Creates a Boolean variable used to know whether this is the first time the user is entering a password.

    while True:  # Starts an infinite loop. The loop continues until the user enters a password that is considered strong and valid.
        if first_attempt:  # Checks if this is the first password attempt.
            psw = input("Enter your password: ")  # Asks the user to enter a password and stores the result inside the psw variable.
            first_attempt = False  # Changes first_attempt to False so that the next time the loop runs, the program uses the second message.
        else:  # Runs this block when it is not the first attempt anymore.
            psw = input("Please enter a valid password: ")  # Asks the user to enter another password after the previous one was not accepted.

        is_valid = True  # Starts by assuming the password is valid. If a serious problem is found, this value will be changed to False.
        suggestions = []  # Creates an empty list that will store suggestions for improving the password.

        if password_in_wordlist(psw):  # Calls the password_in_wordlist function. If it returns True, the password is too common.
            log.append(f"Password '{psw}' found in wordlist.")  # Adds a message to the log list explaining that the password was found in the wordlist.
            suggestions.append("Use a less common password")  # Adds a suggestion telling the user to choose a less common password.
            is_valid = False  # Marks the password as invalid because common passwords are not secure.

        if not (MIN_LENGTH <= len(psw) <= MAX_LENGTH):  # Checks if the password length is outside the allowed range. len(psw) counts the number of characters in the password.
            log.append(f"Password '{psw}' does not meet length requirements.")  # Adds a message to the log list explaining that the password length is not valid.
            suggestions.append(f"Use between {MIN_LENGTH} and {MAX_LENGTH} characters")  # Adds a suggestion explaining the required password length.
            is_valid = False  # Marks the password as invalid because it is too short or too long.

        if any(ord(c) > 127 for c in psw):  # Checks whether at least one character is not part of the standard ASCII range. ord(c) returns the numeric code of a character.
            log.append(f"Password '{psw}' contains non-ASCII characters.")  # Adds a message to the log list explaining that non-ASCII characters were found.
            suggestions.append("Use only ASCII characters")  # Adds a suggestion telling the user to use only ASCII characters.
            is_valid = False  # Marks the password as invalid because it contains non-ASCII characters.

        if any(psw[i] == psw[i + 1] == psw[i + 2] for i in range(len(psw) - 2)): # Checks if at least one sequence of 3 repeated consecutive characters exists, Compares 3 consecutive characters in the password, Iterates through the password while avoiding index overflow
            log.append(f"Password '{psw}' contains 3 repeated characters in a row.") # Stores the validation event in the log
            suggestions.append("Avoid 3 repeated characters in a row") # Adds a suggestion to improve password quality
            is_valid = False # Marks the password as invalid

        results = {  # Creates a dictionary called results. Each key represents a password requirement, and each value is either True or False.
            "symbols": any(c in string.punctuation for c in psw),  # Checks whether the password contains at least one punctuation symbol.
            "numbers": any(c.isdigit() for c in psw),  # Checks whether the password contains at least one number.
            "lowercase": any(c.islower() for c in psw),  # Checks whether the password contains at least one lowercase letter.
            "uppercase": any(c.isupper() for c in psw),  # Checks whether the password contains at least one uppercase letter.
        }  # Closes the results dictionary.

        if not results["symbols"]:  # Checks if the password does not contain any symbols.
            suggestions.append("Add symbols")  # Adds a suggestion telling the user to add at least one symbol.
        if not results["numbers"]:  # Checks if the password does not contain any numbers.
            suggestions.append("Add numbers")  # Adds a suggestion telling the user to add at least one number.
        if not results["lowercase"]:  # Checks if the password does not contain any lowercase letters.
            suggestions.append("Add lowercase letters")  # Adds a suggestion telling the user to add at least one lowercase letter.
        if not results["uppercase"]:  # Checks if the password does not contain any uppercase letters.
            suggestions.append("Add uppercase letters")  # Adds a suggestion telling the user to add at least one uppercase letter.

        score = sum(results.values())  # Calculates the password score. True counts as 1 and False counts as 0, so the score is the number of character-type requirements that were met.

        if score == 4 and is_valid:  # Checks whether all four character-type requirements were met and no serious validation problem was found.
            print("Strong password!")  # Prints that the password is strong.
            return results  # Ends the function and returns the results dictionary because the password has been accepted.

        if score == 3:  # Checks whether exactly three out of four character-type requirements were met.
            print("Medium password. Suggestions:", ", ".join(suggestions))  # Prints that the password is medium and displays the improvement suggestions separated by commas.
        else:  # Runs when the password is not strong and does not have a score of 3.
            print("Weak password. Suggestions:", ", ".join(suggestions))  # Prints that the password is weak and displays the improvement suggestions separated by commas.


analyze_password()  # Calls the main function and starts the program.


                                                                ♰ 𝚢𝚒𝚗 ♰
 

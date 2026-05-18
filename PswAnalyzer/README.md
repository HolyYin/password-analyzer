## 

## &#x20;                                                               ♰ 𝚢𝚒𝚗 ♰

### README - Password Analyzer

##### ==========================

###### *IT IS HIGHLY RECCOMENDED TO OPEN THIS FILE WITH NOTEPAD FOR A BETTER READABILITY*

##### ==========================



This project contains a simple password analyzer written in Python.

The program asks the user to enter a password, checks it against several

security rules, and gives feedback about how strong the password is.



The code is designed to be clear and readable.





#### 1\. What the code is supposed to do

##### ==================================



The program analyzes a password entered by the user and checks whether it meets

basic security requirements.



The program checks:



\- whether the password appears in a wordlist of common passwords;

\- whether the password length is between a minimum and maximum value;

\- whether the password contains non-ASCII characters;

\- whether the password contains repeated consecutive characters;

\- whether the password contains at least one symbol;

\- whether the password contains at least one number;

\- whether the password contains at least one lowercase letter;

\- whether the password contains at least one uppercase letter.



At the end of the analysis, the password is classified as:



\- strong password, if all main requirements are met;

\- medium password, if only one of the character-type requirements is missing;

\- weak password, if two or more character-type requirements are missing or if

&#x20; other important problems are found.



If the password is not valid or not strong enough, the program asks the user to

enter another password.





#### 2\. Input

##### ========



The program receives a password from the user through the input() function.



Example:



Enter your password: Password123!



The program also uses an external wordlist file.

This file contains many common passwords (100k), one password per line.



In the code, the wordlist file path is stored in the WORDLIST\_PATH constant:



D:\\informatica\\python cod\\cybersecurity related stuff\\PswAnalyzer\\100kmostcommon.txt



This file must exist in the specified location. If it does not exist, Python

will raise an error because it will not be able to open the file.





#### 3\. Output

##### =========



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





#### 4\. Code explanation

##### ===================



import string  ***# Imports the string module from the Python standard library. This module contains useful predefined strings, including string.punctuation, which is used to check if the password contains symbols.***



log = \[]  ***# Creates an empty list called log. This list stores messages about problems found during the password analysis.***



MIN\_LENGTH = 8  ***# Defines the minimum allowed password length. In this program, the password must have at least 8 characters.***

MAX\_LENGTH = 32  ***# Defines the maximum allowed password length. In this program, the password must not be longer than 32 characters.***

BASE\_DIR = Path(\_\_file\_\_).resolve().parent      ***# Gets the directory where this script is located***

WORDLIST\_PATH = BASE\_DIR / "100kmostcommon.txt" ***# Builds the path to the wordlist file inside that directory***





def password\_in\_wordlist(psw):  ***# Defines a function that checks whether the password stored in psw appears inside the wordlist file.***

&#x20;   with open(WORDLIST\_PATH, "r", encoding="utf-8", errors="ignore") as file:  ***# Opens the wordlist file in read mode. UTF-8 is used as the encoding, and unreadable characters are ignored to avoid decoding errors.***

&#x20;       for line in file:  ***# Reads the file one line at a time. This is efficient because the whole file is not loaded into memory at once.***

&#x20;           if psw == line.strip():  ***# Compares the user's password with the current line. strip() removes spaces and newline characters from the beginning and end of the line***.

&#x20;               return True  ***# Returns True immediately if the password is found in the wordlist.***

&#x20;   return False  ***# Returns False if the entire file has been checked and the password was not found.***





def analyze\_password():  ***# Defines the main function of the program. This function asks for the password, analyzes it, and prints the result.***

&#x20;   first\_attempt = True  ***# Creates a Boolean variable used to know whether this is the first time the user is entering a password.***



&#x20;   while True:  ***# Starts an infinite loop. The loop continues until the user enters a password that is considered strong and valid.***

&#x20;       if first\_attempt:  ***# Checks if this is the first password attempt.***

&#x20;           psw = input("Enter your password: ")  ***# Asks the user to enter a password and stores the result inside the psw variable.***

&#x20;           first\_attempt = False  ***# Changes first\_attempt to False so that the next time the loop runs, the program uses the second message.***

&#x20;       else:  ***# Runs this block when it is not the first attempt anymore.***

&#x20;           psw = input("Please enter a valid password: ")  ***# Asks the user to enter another password after the previous one was not accepted.***



&#x20;       is\_valid = True  ***# Starts by assuming the password is valid. If a serious problem is found, this value will be changed to False.***

&#x20;       suggestions = \[]  ***# Creates an empty list that will store suggestions for improving the password.***



&#x20;       if password\_in\_wordlist(psw):  ***# Calls the password\_in\_wordlist function. If it returns True, the password is too common.***

&#x20;           log.append(f"Password '{psw}' found in wordlist.")  ***# Adds a message to the log list explaining that the password was found in the wordlist.***

&#x20;           suggestions.append("Use a less common password")  ***# Adds a suggestion telling the user to choose a less common password.***

&#x20;           is\_valid = False  ***# Marks the password as invalid because common passwords are not secure.***



&#x20;       if not (MIN\_LENGTH <= len(psw) <= MAX\_LENGTH):  ***# Checks if the password length is outside the allowed range. len(psw) counts the number of characters in the password.***

&#x20;           log.append(f"Password '{psw}' does not meet length requirements.")  ***# Adds a message to the log list explaining that the password length is not valid.***

&#x20;           suggestions.append(f"Use between {MIN\_LENGTH} and {MAX\_LENGTH} characters")  ***# Adds a suggestion explaining the required password length.***

&#x20;           is\_valid = False  ***# Marks the password as invalid because it is too short or too long.***



&#x20;       if any(ord(c) > 127 for c in psw):  ***# Checks whether at least one character is not part of the standard ASCII range. ord(c) returns the numeric code of a character.***

&#x20;           log.append(f"Password '{psw}' contains non-ASCII characters.")  ***# Adds a message to the log list explaining that non-ASCII characters were found.***

&#x20;           suggestions.append("Use only ASCII characters")  ***# Adds a suggestion telling the user to use only ASCII characters.***

&#x20;           is\_valid = False  ***# Marks the password as invalid because it contains non-ASCII characters.***



&#x20;       if any(psw[i] == psw[i + 1] == psw[i + 2] for i in range(len(psw) - 2)):  **# Checks if at least one sequence of 3 repeated consecutive characters exists, compares 3 consecutive characters in the password, Iterates through the password while avoiding index overflow**

&#x20;           log.append(f"Password '{psw}' contains 3 repeated characters in a row.")  ***# Stores the validation event in the log***

&#x20;           suggestions.append("Avoid 3 repeated characters in a row")  ***# Adds a suggestion to improve password quality***

&#x20;           is\_valid = False  ***# Marks the password as invalid because it contains repeated consecutive characters.***



&#x20;       results = {  ***# Creates a dictionary called results. Each key represents a password requirement, and each value is either True or False.***

&#x20;           "symbols": any(c in string.punctuation for c in psw),  ***# Checks whether the password contains at least one punctuation symbol.***

&#x20;           "numbers": any(c.isdigit() for c in psw),  ***# Checks whether the password contains at least one number.***

&#x20;           "lowercase": any(c.islower() for c in psw),  ***# Checks whether the password contains at least one lowercase letter.***

&#x20;           "uppercase": any(c.isupper() for c in psw),  ***# Checks whether the password contains at least one uppercase letter.***

&#x20;       }  # Closes the results dictionary.



&#x20;       if not results\["symbols"]:  ***# Checks if the password does not contain any symbols.***

&#x20;           suggestions.append("Add symbols")  ***# Adds a suggestion telling the user to add at least one symbol.***

&#x20;       if not results\["numbers"]:  ***# Checks if the password does not contain any numbers.***

&#x20;           suggestions.append("Add numbers")  ***# Adds a suggestion telling the user to add at least one number.***

&#x20;       if not results\["lowercase"]:  ***# Checks if the password does not contain any lowercase letters.***

&#x20;           suggestions.append("Add lowercase letters")  ***# Adds a suggestion telling the user to add at least one lowercase letter.***

&#x20;       if not results\["uppercase"]:  ***# Checks if the password does not contain any uppercase letters.***

&#x20;           suggestions.append("Add uppercase letters")  ***# Adds a suggestion telling the user to add at least one uppercase letter.***



&#x20;       score = sum(results.values())  ***# Calculates the password score. True counts as 1 and False counts as 0, so the score is the number of character-type requirements that were met.***



&#x20;       if score == 4 and is\_valid:  ***# Checks whether all four character-type requirements were met and no serious validation problem was found.***

&#x20;           print("Strong password!")  ***# Prints that the password is strong.***

&#x20;           return results  ***# Ends the function and returns the results dictionary because the password has been accepted.***



&#x20;       if score == 3:  ***# Checks whether exactly three out of four character-type requirements were met.***

&#x20;           print("Medium password. Suggestions:", ", ".join(suggestions))  ***# Prints that the password is medium and displays the improvement suggestions separated by commas.***

&#x20;       else:  ***# Runs when the password is not strong and does not have a score of 3.***

&#x20;           print("Weak password. Suggestions:", ", ".join(suggestions))  ***# Prints that the password is weak and displays the improvement suggestions separated by commas.***





analyze\_password()  ***# Calls the main function and starts the program.***





## &#x20;                                                               ♰ 𝚢𝚒𝚗 ♰




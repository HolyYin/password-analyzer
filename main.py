import string
from pathlib import Path

log = []

MIN_LENGTH = 8
MAX_LENGTH = 32
BASE_DIR = Path(__file__).resolve().parent
WORDLIST_PATH = BASE_DIR / "100kmostcommon.txt"


def password_in_wordlist(psw):
    with open(WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            if psw == line.strip():
                return True
    return False


def analyze_password():
    first_attempt = True

    while True:
        if first_attempt:
            psw = input("Enter your password: ")
            first_attempt = False
        else:
            psw = input("Please enter a valid password: ")

        is_valid = True
        suggestions = []

        if password_in_wordlist(psw):
            log.append(f"Password '{psw}' found in wordlist.")
            suggestions.append("Use a less common password")
            is_valid = False

        if not (MIN_LENGTH <= len(psw) <= MAX_LENGTH):
            log.append(f"Password '{psw}' does not meet length requirements.")
            suggestions.append(f"Use between {MIN_LENGTH} and {MAX_LENGTH} characters")
            is_valid = False

        if any(ord(c) > 127 for c in psw):
            log.append(f"Password '{psw}' contains non-ASCII characters.")
            suggestions.append("Use only ASCII characters")
            is_valid = False

        if any(psw[i] == psw[i + 1] for i in range(len(psw) - 1)):
            log.append(f"Password '{psw}' contains repeated characters.")
            suggestions.append("Avoid repeated characters")
            is_valid = False

        results = {
            "symbols": any(c in string.punctuation for c in psw),
            "numbers": any(c.isdigit() for c in psw),
            "lowercase": any(c.islower() for c in psw),
            "uppercase": any(c.isupper() for c in psw),
        }

        if not results["symbols"]:
            suggestions.append("Add symbols")
        if not results["numbers"]:
            suggestions.append("Add numbers")
        if not results["lowercase"]:
            suggestions.append("Add lowercase letters")
        if not results["uppercase"]:
            suggestions.append("Add uppercase letters")

        score = sum(results.values())

        if score == 4 and is_valid:
            print("Strong password!")
            return results

        if score == 3:
            print("Medium password. Suggestions:", ", ".join(suggestions))
        else:
            print("Weak password. Suggestions:", ", ".join(suggestions))


analyze_password()
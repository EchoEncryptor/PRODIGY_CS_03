import re

SPECIAL_CHARACTERS = r"!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"


def evaluate_password_strength(password: str) -> dict:
    """
    Evaluate the strength of a given password.

    Returns a dictionary with:
      - score: int (0-5)
      - verdict: str (Weak, Moderate, Strong)
      - feedback: list of str suggestions
    """
    feedback = []
    score = 0

    # Check length
    length = len(password)
    if length >= 8:
        score += 1
    else:
        feedback.append('Make your password at least 8 characters long.')

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('Include at least one lowercase letter.')

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append('Include at least one uppercase letter.')

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('Include at least one number.')

    # Check for special characters
    if re.search(f'[{re.escape(SPECIAL_CHARACTERS)}]', password):
        score += 1
    else:
        feedback.append('Include at least one special character (e.g., !, @, #, etc.).')

    # Determine verdict
    if score <= 2:
        verdict = 'Weak'
    elif 3 <= score <= 4:
        verdict = 'Moderate'
    else:
        verdict = 'Strong'

    return {
        'score': score,
        'verdict': verdict,
        'feedback': feedback
    }


def main():
    print('Password Strength Checker')
    pwd = input('Enter a password to evaluate: ')
    result = evaluate_password_strength(pwd)

    print(f"\nScore: {result['score']} / 5")
    print(f"Strength: {result['verdict']}")
    if result['feedback']:
        print('\nSuggestions to improve your password:')
        for item in result['feedback']:
            print(f" - {item}")


if __name__ == '__main__':
    main()

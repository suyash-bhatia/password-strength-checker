def check_password(password):
    score = 0
    feedback = []

    # Remove leading/trailing spaces
    password = password.strip()

    # Common passwords check
    common_passwords = ["123456", "password", "qwerty"]
    if password in common_passwords:
        return "Very Weak", ["This is a very common password"]

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Special character check
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    # Strength decision
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# Run program
password = input("Enter your password: ")
strength, feedback = check_password(password)

print("Password Strength:", strength)

if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)

import string
import secrets


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    """Generate a password using the character types selected by the user."""
    character_groups = []

    if use_lower:
        character_groups.append(string.ascii_lowercase)
    if use_upper:
        character_groups.append(string.ascii_uppercase)
    if use_digits:
        character_groups.append(string.digits)
    if use_symbols:
        character_groups.append(string.punctuation)

    all_characters = "".join(character_groups)

    # Include at least one character from each selected group.
    password_characters = [
        secrets.choice(group) for group in character_groups
    ]

    # Fill the remaining positions.
    while len(password_characters) < length:
        password_characters.append(secrets.choice(all_characters))

    # Randomize the order of characters.
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def ask_yes_no(prompt):
    """Ask until the user enters y or n."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter y for yes or n for no.")


def main():
    print("=" * 42)
    print("          PASSWORD GENERATOR")
    print("=" * 42)

    while True:
        try:
            length = int(input("Enter password length (minimum 1): "))
            if length < 1:
                print("Please enter a positive whole number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nChoose the character types to include:")
    use_lower = ask_yes_no("Include lowercase letters (a-z)? (y/n): ")
    use_upper = ask_yes_no("Include uppercase letters (A-Z)? (y/n): ")
    use_digits = ask_yes_no("Include numbers (0-9)? (y/n): ")
    use_symbols = ask_yes_no("Include special symbols (!@#$...)? (y/n): ")

    selected_groups = [
        use_lower, use_upper, use_digits, use_symbols
    ]

    if not any(selected_groups):
        print("\nError: Select at least one character type.")
        return

    selected_types = sum(selected_groups)
    if length < selected_types:
        print(
            f"\nError: The password length must be at least "
            f"{selected_types} for the selected character types."
        )
        return

    password = generate_password(
        length, use_lower, use_upper, use_digits, use_symbols
    )

    print("\n" + "=" * 42)
    print("Your generated password is:")
    print(password)
    print("=" * 42)

    if ask_yes_no("\nGenerate another password? (y/n): "):
        print()
        main()
    else:
        print("Thank you for using Password Generator!")


if __name__ == "__main__":
    main()

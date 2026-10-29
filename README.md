# Password Generator Using Python

A beginner-friendly command-line project that creates random passwords using Python's built-in `string` and `secrets` modules.

## Features
- Choose the password length.
- Choose lowercase letters, uppercase letters, digits, and/or special symbols.
- Uses `secrets` for security-oriented random selection.
- Checks invalid input and missing character selections.
- Option to generate another password.

## Requirements
- Python 3.10 or newer (the project uses only Python standard-library modules).
- Visual Studio Code or another editor is optional.

No extra packages need to be installed.

## Run in VS Code
1. Extract the ZIP file.
2. Open the `Password_Generator` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:
   ```powershell
   python password_generator.py
   ```
   If `python` is not recognized, try:
   ```powershell
   py password_generator.py
   ```
5. Enter the password length and answer the character-type prompts with `y` or `n`.

## Example
Your output will look similar to this (the generated password will differ):

```text
PASSWORD GENERATOR
Enter password length (minimum 1): 12
Include lowercase letters (a-z)? (y/n): y
Include uppercase letters (A-Z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include special symbols (!@#$...)? (y/n): y

Your generated password is:
m8@Q2#zL5$pR
```

## Files
- `password_generator.py` — the complete Python application.
- `README.md` — project overview and run instructions.
- `PROJECT_REPORT.md` — project report for study/submission.
- `VIVA_QUESTIONS.md` — sample viva questions and answers.

## Security note
The program displays the password in the terminal. Do not share it or save it in an unprotected text file. For important accounts, use a reputable password manager.

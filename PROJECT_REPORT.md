# Project Report: Password Generator Using Python

## 1. Introduction
A Password Generator is an application that creates random passwords based on user preferences. The user chooses the desired length and which character types to include.

## 2. Problem Statement
Creating strong passwords manually can be difficult. This project provides a simple way to generate random passwords with a chosen length and character complexity.

## 3. Objectives
- Generate random passwords automatically.
- Let users choose password length.
- Support lowercase letters, uppercase letters, numbers, and special symbols.
- Validate user input.
- Practise fundamental Python concepts.

## 4. Technologies Used
- Python
- Python standard-library modules: `string` and `secrets`
- Visual Studio Code (optional editor)

## 5. Hardware and Software Requirements
- Computer or laptop
- Python installed
- Windows, macOS, or Linux
- VS Code or another text editor (optional)

## 6. Method / Algorithm
1. Start the program.
2. Ask for password length.
3. Validate that the length is a positive whole number.
4. Ask which character types to include.
5. Ensure at least one character type is selected.
6. Ensure the length is sufficient for the selected types.
7. Select at least one character from each selected type.
8. Fill the remaining positions with random characters from the selected pool.
9. Shuffle the characters and display the password.
10. Ask whether the user wants to generate another password.
11. End the program.

## 7. Python Concepts Used
- Variables and data types
- Input and output
- Functions
- Conditional statements
- Loops
- Lists and strings
- Exception handling
- Modules

## 8. Advantages
- Simple to use
- Fast password generation
- Customizable length and character types
- Uses Python's `secrets` module for security-oriented random selection
- Requires no third-party packages

## 9. Limitations
- Runs in the terminal and has no graphical interface.
- Does not store passwords in a password manager.
- Does not check a website's password rules.

## 10. Future Enhancements
- Add a graphical interface using Tkinter.
- Add a copy-to-clipboard button.
- Add a password-strength indicator.
- Add secure password-manager integration.

## 11. Conclusion
The Password Generator demonstrates how Python can generate random passwords according to user choices. It provides practical experience with functions, loops, conditions, lists, modules, and exception handling.

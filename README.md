# Simple Calculator in Python

This project is a basic command-line calculator implemented in Python. It allows users to perform simple arithmetic operations: addition, subtraction, multiplication, and division. This is a straightforward application demonstrating fundamental Python programming concepts.

## Problem Statement/Motivation

The motivation behind this project is to create a simple, functional calculator using Python. It serves as a basic exercise in handling user input, conditional logic, and arithmetic operations in Python. This type of project is often a starting point for learning programming and understanding fundamental computational tasks.

## Features Implemented

* **Addition:** Allows users to add two numbers.
* **Subtraction:** Allows users to subtract one number from another.
* **Multiplication:** Allows users to multiply two numbers.
* **Division:** Allows users to divide one number by another.
* **User-Friendly Interface:** Provides a simple, text-based menu for selecting operations.
* **Input Validation:** Includes basic validation to ensure the user selects a valid operation.

## Technologies Used

* **Python:** The primary programming language used for the entire application.

## Setup and Installation Instructions

1.  **Prerequisites:** Ensure you have Python installed on your system. You can download it from the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).
2.  **Download the Code:** Save the provided Python code as a `.py` file (e.g., `calculator.py`).
3.  **Run the Application:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command:
    ```bash
    python calculator.py
    ```
4.  Follow the on-screen prompts to perform calculations.

## Usage/Examples

1.  Run the `calculator.py` script.
2.  You will be presented with a menu of operations:
    ```
    Welcome To A Simple Caculator

    1. for ADDING
    2. for SUBTRACTING
    3. for MULTIPLYING
    4. FOR DIVING

    Select an operation to perform:
    ```
3.  Enter the number corresponding to the desired operation (1, 2, 3, or 4).
4.  If you select a valid operation, you will be prompted to enter the first and second numbers.
5.  The calculator will then display the result of the chosen operation.

    **Example (Addition):**
    ```
    Select an operation to perform: 1

    Enter First Number: 5
    Enter Second Number: 3
    The sum is 8
    ```

    **Example (Invalid Input):**
    ```
    Select an operation to perform: 5
    That is an invalid selection.
    Enter 1, 2, 3, 4: 2

    Enter First Number: 10
    Enter Second Number: 4
    The difference is 6
    ```

## Challenges & Learnings (Optional but beneficial)

While this is a simple calculator, potential challenges during development might have included:

* **Handling potential errors:** Implementing more robust error handling, such as handling non-numeric input or division by zero.
* **Improving user experience:** Creating a more interactive or graphical user interface.
* **Expanding functionality:** Adding more advanced mathematical operations.

This project served as a good exercise in understanding basic Python syntax, input/output operations, conditional statements (`if`, `elif`, `else`), and loop structures (`while`).
```

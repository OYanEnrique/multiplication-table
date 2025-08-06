# multiplication-table
A simple Python script that generates and displays the multiplication table for a user-provided number, from 0 to 10.

# 🧮 Multiplication Table Generator

This is a simple command-line program written in Python that generates the full multiplication table (from 0 to 10) for any integer the user provides.

The script prompts the user for a number and then uses a `for` loop to iterate from 0 to 10, printing the result of each multiplication. 

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `multiplication_table.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python multiplication_table.py
    ```
5.  Enter the number for which you want to see the multiplication table and press Enter. The program will immediately display the complete table.

## Program Logic

* **User Input:** The program first asks the user to provide a number (`user_number`) which will be the base for the table.
* **Looping:** A `for` loop is used with `range(0, 11)` to create a sequence of numbers from 0 to 10.
* **Calculation and Output:** In each iteration of the loop, the program multiplies the `user_number` by the current loop number (`multiplication_number`) and prints the formatted multiplication line (e.g., `5 x 3 = 15`).

Smart Transport Load Balancing System:
Project Description:
The Smart Transport Load Balancing System is a Python-based program developed to simulate how a logistics company analyzes package weights before transportation. The system checks each package, categorizes it based on predefined weight ranges, and applies a personalized adjustment rule to maintain a balanced and safe loading plan.
The final output changes for every user because the system applies a rule based on the length of the user’s name.

Objective:
The objective of this project is to:
Accept package weights from the user
Classify weights into safety categories
Apply a Personalized Logic Index (PI)
Generate a final loading report showing balanced transport data
Program Workflow:

The user enters their full name.
The program calculates L, which is the number of characters excluding spaces.
The PLI value is calculated using:

PLI = L % 3

The user provides package weights as input.
Each weight is processed using loops and conditional statements.
Packages are categorized into:

Invalid Entries (< 0)

Very Light (0–5)

Normal Load (6–25)

Heavy Load (26–60)

Overload (> 60)

Based on the PLI value, one of the following rules is applied:

Rule A (PLI = 0): Overload items are moved to invalid entries.

Rule B (PLI = 1): Very light items are removed.

Rule C (PLI = 2): Only normal and heavy loads remain.

The final categorized loading report is displayed.
Personalization Details

Full Name: Likhitha

L Value: 8

PLI Value: 2

Applied Rule: Rule C
Output Generated

The program displays:

L value and PLI value

Applied personalization rule

Total number of valid weights

Number of affected items after rule application

Final categorized lists of packages

Concepts Used:

Python Lists

For Loop and While Loop

Conditional Statements (if–elif–else)

User Input Processing

Basic Data Validation

Constraints Followed:

No list comprehension used

No dictionaries or sets

No built-in functions such as sum(), max(), or min()

No sorting functions

Output is dynamically generated

Conclusion:

This project demonstrates how programming logic can be applied to solve a real-world logistics problem. By combining classification rules with personalization logic, the system ensures a balanced and safe transport loading plan.



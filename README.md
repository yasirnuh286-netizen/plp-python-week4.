# PLP Python Week 4 Assignment: Grades, Eligibility & Smart Decisions

This repository contains Python programs demonstrating multi-way decisions, logical operators, input validation, and nested conditionals.

## Files Description
* `grade_classifier.py`: Validates a score (0–100) and converts it to a letter grade (A–F).
* `eligibility_checker.py`: Checks club membership eligibility based on age and parental consent using logical operators (`and`, `or`, `not`).
* `atm_menu.py`: Simulates an ATM withdrawal using nested decisions to verify a PIN and check account balance.

## Reflection
`elif` is better than using several separate `if` statements because it creates mutually exclusive conditions. With multiple `if` statements, Python evaluates every single condition regardless of whether a previous condition was met, which is inefficient and can lead to bugs (e.g., matching multiple grade ranges). `elif` ensures that once a condition evaluates to `True`, the remaining conditions are skipped entirely.

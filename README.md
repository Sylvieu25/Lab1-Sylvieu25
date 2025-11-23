# Lab 1 – Grade Generator Calculator

This project is part of the **Introduction to Python Programming and Databases** 
 It includes:

---

##  Part 1: Python Script – `grade-generator.py`

This script allows users to enter multiple assignment records and calculates:

- ✅ Weighted grade per assignment
- ✅ Total Formative (FA) and Summative (SA) scores
- ✅ Final grade and GPA
- ✅ Pass/Fail status based on category thresholds

It also:

- Validates inputs (grade range, category type, positive weight)
- Saves all assignment data to a CSV file named `grades.csv`
- Prints a clear summary to the console

---

##  Part 2: Shell Script – `organizer.sh`

This script organizes and archives CSV files:

- Checks if an `archive/` folder exists (creates it if missing)
- Finds all `.csv` files in the current directory
- Renames each file with a timestamp (e.g., `grades-20251123-080000.csv`)
- Logs the action and file contents into `organizer.log`
- Moves the renamed file into the `archive/` directory

---

##  How to Run

### Python Script
```bash
python3 grade-generator.py


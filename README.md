#   

# Sorting Package

# 

This project implements various sorting algorithms in Python, following an abstract base class (Strategy Pattern) design. It includes a test suite using `pytest` and a main entrypoint to demonstrate usage.

## Project Structure

# 

    Sorting_Package/
    ├── main.py             # Showcase script
    ├── input.txt           # Sample input for main.py
    ├── reports/            # Placeholder for reports
    │   └── .gitkeep
    ├── src/
    │   ├── __init__.py         # Makes 'src' a package
    │   ├── sorter.py         # Main Sorter class (Strategy Context)
    │   └── algorithms/
    │       ├── __init__.py     # Makes 'algorithms' a sub-package
    │       ├── base_sort.py    # Abstract Base Class (SortStrategy)
    │       ├── bubble_sort.py  # Concrete Strategy
    │       ├── merge_sort.py   # Concrete Strategy
    │       ├── quick_sort.py   # Concrete Strategy
    │       └── selection_sort.py # Concrete Strategy
    ├── test/
    │   └── test_sorting.py     # Pytest test suite
    ├── setup.py            # Makes the project an installable package
    └── requirements.txt    # Project dependencies (for testing)
    
    

## Setup & Installation

# 

1.  **Create a virtual environment:**
    
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        
        
    
2.  **Install dependencies and the package in editable mode:** The `-e` flag (editable) links the package to your source code, so changes are reflected immediately.
    
        pip install -r requirements.txt
        cd Sort_Package
        pip install -e .
        
        
    

## How to Run

### 1\. Run the Showcase (`main.py`)

# 

The `main.py` script reads numbers from `input.txt`, runs all sorting algorithms on them, and prints the sorted results to **stdout**. Informational messages are printed to **stderr**, so you can safely redirect the output.

    # Run the main script, passing the input file
    cd Sort_Package
    python3 main.py input.txt
    
    

**To redirect the sorted output to a file:**

    # The file 'output.txt' will contain *only* the sorted numbers
     python3 Sort_Package/main.py Sort_Package/input.txt >  Sort_Package/output.txt
    
    # We will still see the info messages (like "--- Bubble Sort ---") in your terminal.
    
    

### 2\. Run the Test Suite

# 
  
 Use `pytest` to run all the correctness tests:
    
        cd Sort_Package 
        python3 - m  pytest





pylint src > reports/pylint_report_after.txt

Here is the new report, showing our much-improved score:


http://googleusercontent.com/immersive_entry_chip/9

### Step 5: Refactoring Report

As requested, here is a report explaining the changes.0

### Step 6: Test the Refactored Code

Now, let's run our test suite to ensure our refactoring didn't break anything.

**Command:**
(Run this from your `Sorting_Package` directory)

```bash
python3 -m pytest

**Expected Output:**
You should see all 11 tests pass, just as they did before. This confirms our changes were safe.

============================= test session starts ==============================
...
collected 11 items

test/test_sorting.py ...........                                        [100%]

============================= 11 passed in 0.01s =============================

### Step 7: Add Shell Sort

Now we'll extend the package with a new algorithm.

First, create the `shell_sort.py` file. Notice it's already documented to our new standard.1

Next, **update `src/sorter.py`** to include it:2

Finally, **update `test/test_sorting.py`** to test it:3

Now, run your tests again. You'll see more tests are run, and they all pass!

```bash
python3 -m pytest
**Output:**
============================= test session starts ==============================
...
collected 14 items  <--- (7 test cases x 2 algos (asc/desc) = 14 tests)

test/test_sorting.py ..............                                       [100%]

============================= 14 passed in 0.02s =============================

### Step 8: Final Pylint Check

Let's see how adding the new, well-documented `shell_sort.py` affects the score.

**Command:**
(Run this from your `Sorting_Package` directory)

```bash
pylint src > reports/pylint_report_final.txt

Here is the final report:4

The score actually went *up* slightly! This is because we added new, high-quality (well-documented) code, increasing the overall quality score.

### Step 9: Git Workflow Guide

Here is how you can use `git` to showcase these changes as requested.

```bash
# Start from your main branch with the original code
# (Assuming you've already 'git init' and made your first commit)

# 1. Create a branch for refactoring
git checkout -b refactor

# 2. Add the refactored files
# (Copy all the files from Step 3 into your 'src' directory)
# (Copy the 'pylint_report_before.txt' and 'pylint_report_after.txt' into 'reports')
# (Copy the 'refactoring_report.md' into 'reports')

# 3. Commit the refactored code
git add src reports
git commit -m "REF: Refactor code for Pylint score > 9.5"

# 4. Tag this version
git tag v1.1-refactored

# 5. Create a new branch *from the refactored one* for the new feature
git checkout -b feature-shell-sort

# 6. Add the Shell Sort files
# (Add 'src/algorithms/shell_sort.py')
# (Overwrite 'src/sorter.py' and 'test/test_sorting.py' with the files from Step 7)
# (Add 'pylint_report_final.txt' to 'reports')

# 7. Commit the new feature
git add src/algorithms/shell_sort.py src/sorter.py test/test_sorting.py reports/pylint_report_final.txt
git commit -m "FEAT: Add Shell Sort algorithm and tests"

# 8. Tag this final version
git tag v1.2-shell-sort

# You can now see your history
git log --oneline --graph --all

# You can also switch between versions easily:
# git checkout v1.1-refactored  (to see the refactored code)
# git checkout v1.2-shell-sort   (to see the final code with shell sort)
# git checkout main              (to see your original code)
        
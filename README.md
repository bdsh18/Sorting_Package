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
        
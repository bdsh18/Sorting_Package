"""
Main Showcase Script

This script demonstrates the Sorter class by reading an input file,
running various sorting algorithms, and printing the results.
"""
import sys

# We update the import path to find the 'src' package
# This is a common pattern for running a script from the project root.
# A more robust way is installing with 'pip install -e .' and
# just 'from src.sorter import Sorter'
try:
    from src.sorter import Sorter
except ImportError:
    print("Error: 'src' module not found.", file=sys.stderr)
    print("Please make sure you are running this from the 'Sorting_Package' directory", file=sys.stderr)
    print("and have installed the package with: pip install -e .", file=sys.stderr)
    sys.exit(1)


def main():
    """
    Main function to run the sorting showcase.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            # Read all lines, strip whitespace, and convert to int
            # Filter out empty lines
            lines = f.readlines()
            numbers = [int(line.strip()) for line in lines if line.strip()]

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Input file contains invalid data: {e}", file=sys.stderr)
        sys.exit(1)

    my_sorter = Sorter()
    
    # --- THIS IS THE LINE TO CHANGE ---
    # Add 'shell' to this list
    algorithms = ["bubble", "selection", "quick", "merge", "shell"]
    
    list_size = len(numbers)

    for algo in algorithms:
        print(f"--- {algo.capitalize()} Sort ---", file=sys.stderr)
        
        # --- Ascending ---
        print(f"Ascending (size={list_size}):", file=sys.stderr)
        sorted_asc = my_sorter.sort(
            input_list=numbers,
            algorithm_name=algo,
            ascending=True,
            size_of_list=list_size
        )
        # Print sorted numbers to stdout
        for num in sorted_asc:
            print(num)

        # --- Descending ---
        print(f"\nDescending (size={list_size}):", file=sys.stderr)
        sorted_desc = my_sorter.sort(
            input_list=numbers,
            algorithm_name=algo,
            ascending=False,
            size_of_list=list_size
        )
        # Print sorted numbers to stdout
        for num in sorted_desc:
            print(num)
        
        print("-" * (len(algo) + 10), file=sys.stderr)

    # --- Showcase error handling ---
    print("\n--- Showcasing Expected Errors ---", file=sys.stderr)
    try:
        my_sorter.sort([1, 2], "magic", True)
    except ValueError as e:
        print(f"Caught expected error: {e}", file=sys.stderr)
        
    try:
        my_sorter.sort([1, "a"], "bubble", True)
    except TypeError as e:
        print(f"Caught expected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
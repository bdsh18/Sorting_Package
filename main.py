import sys
from typing import List

# This import works because 'main.py' and 'src/'
# are in the same directory ('Sorting_Package/'),
# and the directory where you run the script ('Sorting_Package/')
# is added to the Python path.
try:
    from src import Sorter
except ImportError:
    print("--- IMPORT ERROR ---", file=sys.stderr)
    print(f"Error: Could not import 'Sorter' from 'src'.", file=sys.stderr)
    print(f"Current Python Path: {sys.path}", file=sys.stderr)
    print("Please ensure 'src' is a package (has __init__.py) and is in the same directory as main.py", file=sys.stderr)
    print("If you installed the package with 'pip install -e .', try re-activating your virtual environment.", file=sys.stderr)
    sys.exit(1)

def load_input_file(filepath: str) -> List[int]:
    """Reads a file with one number per line and returns a list of integers."""
    numbers = []
    with open(filepath, 'r') as f:
        for line in f:
            # Remove whitespace and skip empty lines
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # Try to convert to int, warning on failure
            try:
                numbers.append(int(clean_line))
            except ValueError:
                print(f"Warning: Skipping invalid non-integer line '{clean_line}'", file=sys.stderr)
    return numbers

def main():
    """
    Main function to showcase the Sorter class.
    """
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <input_file_path>", file=sys.stderr)
        print("Example: python main.py input.txt", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    
    # Load numbers from the specified file
    try:
        numbers_to_sort = load_input_file(input_file)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {e}", file=sys.stderr)
        sys.exit(1)

    if not numbers_to_sort:
        print("Input file is empty or contains no valid integers. Exiting.", file=sys.stderr)
        return

    # Initialize the sorter
    my_sorter = Sorter()
    
    # List of algorithms to showcase
    algorithms = ["bubble", "selection", "quick", "merge"]
    
    # --- Showcase all algorithms ---
    for algo in algorithms:
        print(f"--- {algo.capitalize()} Sort (Ascending) ---", file=sys.stderr)
        try:
            # Call the sorter
            sorted_asc = my_sorter.sort(
                input_list=numbers_to_sort,
                algorithm_name=algo,
                ascending=True,
                size_of_list=len(numbers_to_sort) # Pass explicit size
            )
            
            # Print sorted list to STDOUT (for redirection)
            for num in sorted_asc:
                print(num)

            print(f"\n--- {algo.capitalize()} Sort (Descending) ---", file=sys.stderr)
            sorted_desc = my_sorter.sort(
                input_list=numbers_to_sort,
                algorithm_name=algo,
                ascending=False
            )
            
            # Print sorted list to STDOUT
            for num in sorted_desc:
                print(num)

            print("\n", file=sys.stderr) # Add a newline for readability in stderr

        except (ValueError, TypeError) as e:
            print(f"Error running {algo} sort: {e}", file=sys.stderr)
            
    # --- Showcase error handling ---
    print("--- Showcasing Expected Errors ---", file=sys.stderr)
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
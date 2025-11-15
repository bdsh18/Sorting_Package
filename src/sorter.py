"""
Main Sorter Class Module

Defines the Sorter class, the main interface for accessing sorting algorithms.
"""
import sys
from typing import List, Any
from .algorithms import (
    BaseSort, BubbleSort, SelectionSort, QuickSort, MergeSort, ShellSort
)

# pylint: disable=too-few-public-methods
class Sorter:
    """
    A factory class to access different sorting algorithms.

    This class validates input and delegates sorting to the specified
    algorithm implementation.
    """

    # --- FIX: Moved from __init__ to class level for constants ---
    # Define INT32 range constraints (Requirement 5)
    INT32_MIN = -2**31
    INT32_MAX = 2**31 - 1
    MAX_ELEMENTS = 2 * 10**5
    # --- END FIX ---

    def __init__(self):
        """Initializes the Sorter with a dictionary of available algorithms."""
        self._algorithms: dict[str, BaseSort] = {
            "bubble": BubbleSort(),
            "selection": SelectionSort(),
            "quick": QuickSort(),
            "merge": MergeSort(),
            "shell": ShellSort(),
        }

    def _validate_input(self, data: List[Any], size_of_list: int | None) -> None:
        """
        Private helper to validate the input list based on project constraints.
        - Requirement 7: Only Integers
        - Requirement 5: INT32 range and element count
        - Requirement 6c: Validate list size
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")

        # Requirement 6c: Validate provided size if given
        if size_of_list is not None and len(data) != size_of_list:
            raise ValueError(
                f"Provided 'size_of_list' ({size_of_list}) does not "
                f"match the actual length of 'input_list' ({len(data)})."
            )

        if not data:
            return  # Empty list is valid

        # Requirement 7: Check for non-integer types
        # --- FIX C0325: Removed unnecessary parenthesis around 'isinstance' ---
        if not all(isinstance(x, int) for x in data):
        # --- END FIX ---
            raise TypeError("All elements in the list must be integers.")

        # Requirement 5: Check element count
        if len(data) >= self.MAX_ELEMENTS:
            print(
                f"Warning: List size ({len(data)}) exceeds "
                f"project limit ({self.MAX_ELEMENTS}).",
                file=sys.stderr
            )

        # Requirement 5: Check INT32 range
        for x in data:
            if not (self.INT32_MIN <= x <= self.INT32_MAX):
                raise ValueError(
                    f"Element {x} is outside the allowed INT32 range "
                    f"[{self.INT32_MIN}, {self.INT32_MAX}]"
                )

    def sort(
        self,
        input_list: List[Any],
        algorithm_name: str,
        ascending: bool,
        size_of_list: int | None = None
    ) -> List[int]:
        """
        Sorts a list of integers using the specified algorithm.

        Args:
            input_list: The list of data to sort (Requirement 6d).
            algorithm_name: Name of the algorithm to use (Requirement 6b).
            ascending: Sort ascending if True, descending if False (Requirement 6a).
            size_of_list: The provided size of the list (Requirement 6c).

        Returns:
            A *new* sorted list (Requirement 8).
        """
        # Run all validations (Requirements 5, 6c, 7)
        self._validate_input(input_list, size_of_list)

        # Requirement 6b: Select the sorting strategy
        strategy_instance = self._algorithms.get(algorithm_name.lower())

        if not strategy_instance:
            raise ValueError(
                f"Unknown algorithm: {algorithm_name}. "
                f"Available algorithms are: {list(self._algorithms.keys())}"
            )

        # Requirement 8: Create a copy to return a new list and avoid
        # modifying the original input_list.
        list_copy = list(input_list)

        # Execute the sort
        return strategy_instance.sort(list_copy, ascending)

# --- FIX C0304: Added final newline ---
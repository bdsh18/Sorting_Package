import sys
from typing import List, Dict, Type
from .algorithms.base_sort import SortStrategy
from .algorithms.bubble_sort import BubbleSort
from .algorithms.selection_sort import SelectionSort
from .algorithms.quick_sort import QuickSort
from .algorithms.merge_sort import MergeSort

class Sorter:
    """
    The "Context" class that uses a sorting strategy.
    This class fulfills requirements 4, 5, 6, and 7.
    """
    def __init__(self):
        """Initializes the Sorter with a mapping of algorithm names to their classes."""
        self._strategies: Dict[str, Type[SortStrategy]] = {
            "bubble": BubbleSort,
            "selection": SelectionSort,
            "quick": QuickSort,
            "merge": MergeSort,
        }
        
        # Define INT32 range constraints
        self._INT32_MIN = -2**31
        self._INT32_MAX = 2**31 - 1
        self._MAX_ELEMENTS = 2 * 10**5

    def _validate_input(self, data: List) -> None:
        """
        Private helper to validate the input list based on project constraints.
        - Requirement 7: Only Integers
        - Requirement 5: INT32 range and element count
        """
        if not data:
            return  # Empty list is valid
            
        # Requirement 7: Check for non-integer types
        if not all(isinstance(x, int) for x in data):
            raise TypeError("All elements in the list must be integers.")

        # Requirement 5: Check element count
        if len(data) >= self._MAX_ELEMENTS:
            # Using print to stderr as a warning, not a hard stop
            print(f"Warning: List size ({len(data)}) is large, sorting may be slow.", file=sys.stderr)

        # Requirement 5: Check INT32 range
        for x in data:
            if not (self._INT32_MIN <= x <= self._INT32_MAX):
                raise ValueError(
                    f"Element {x} is outside the allowed INT32 range "
                    f"[{self._INT32_MIN}, {self._INT32_MAX}]"
                )

    def sort(self, input_list: List, algorithm_name: str, ascending: bool, size_of_list: int = None) -> List[int]:
        """
        Sorts a list of integers using the specified algorithm.

        Args:
            input_list (List): The list of data to sort (Requirement 6d).
            algorithm_name (str): Name of the algorithm to use (Requirement 6b).
            ascending (bool): Sort ascending if True, descending if False (Requirement 6a).
            size_of_list (int, optional): The provided size of the list (Requirement 6c).

        Returns:
            List[int]: A *new* sorted list (Requirement 8).
        """
        
        # Requirement 6c: Validate provided size if given
        if size_of_list is not None and len(input_list) != size_of_list:
            raise ValueError(
                f"Provided 'size_of_list' ({size_of_list}) does not "
                f"match the actual length of 'input_list' ({len(input_list)})."
            )
            
        # Run validations (Requirements 5, 7)
        self._validate_input(input_list)

        # Requirement 6b: Select the sorting strategy
        strategy_class = self._strategies.get(algorithm_name.lower())
        
        if not strategy_class:
            raise ValueError(
                f"Unknown algorithm: {algorithm_name}. "
                f"Available algorithms are: {list(self._strategies.keys())}"
            )

        # Create an instance of the chosen strategy
        strategy_instance = strategy_class()
        
        # Execute the sort
        # Requirement 8: The strategy is responsible for returning a new list.
        return strategy_instance.sort(input_list, ascending)
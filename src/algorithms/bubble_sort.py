"""Implementation of the Bubble Sort algorithm."""
from typing import List
from .base_sort import BaseSort

class BubbleSort(BaseSort):
    """Implements the Bubble Sort algorithm."""
    def _sort_logic(self, array: List[int]) -> List[int]:
        """
        Sorts a list using the Bubble Sort algorithm (ascending).

        Args:
            array: The list of integers to sort.

        Returns:
            The sorted list.
        """
        n = len(array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                break  # List is already sorted
        return array
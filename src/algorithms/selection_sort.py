"""Implementation of the Selection Sort algorithm."""
from typing import List
from .base_sort import BaseSort

class SelectionSort(BaseSort):
    """Implements the Selection Sort algorithm."""
    def _sort_logic(self, array: List[int]) -> List[int]:
        """
        Sorts a list using the Selection Sort algorithm (ascending).
        Args:
            array: The list of integers to sort.
        Returns:
            The sorted list.
        """
        n = len(array)
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            idx_to_swap = i
            for j in range(i + 1, n):
                if array[j] < array[idx_to_swap]:
                    idx_to_swap = j    
            # Swap the found minimum element with the first element
            array[i], array[idx_to_swap] = array[idx_to_swap], array[i]
        return array
    
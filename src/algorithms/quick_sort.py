"""Implementation of the Quick Sort algorithm."""
from typing import List
from .base_sort import BaseSort

class QuickSort(BaseSort):
    """Implements the Quick Sort algorithm."""
    def _sort_logic(self, array: List[int]) -> List[int]:
        """
        Sorts a list using the Quick Sort algorithm (ascending).
        Args:
            array: The list of integers to sort.
        Returns:
            The sorted list.
        """
        self._quick_sort_recursive(array, 0, len(array) - 1)
        return array
    def _quick_sort_recursive(self, array: List[int], low: int, high: int):
        """
        Recursive helper function for Quick Sort.
        Args:
            array: The list being sorted (modified in-place).
            low: The starting index of the partition.
            high: The ending index of the partition.
        """
        if low < high:
            # pi is partitioning index, array[pi] is now at right place
            pi = self._partition(array, low, high)
            # Separately sort elements before and after partition
            self._quick_sort_recursive(array, low, pi - 1)
            self._quick_sort_recursive(array, pi + 1, high)
    def _partition(self, array: List[int], low: int, high: int) -> int:
        """
        Helper function to partition the array.
        This uses the last element as the pivot.
        Args:
            array: The list being sorted (modified in-place).
            low: The starting index.
            high: The ending index (pivot element).
        Returns:
            The partitioning index.
        """
        pivot = array[high]
        i = low - 1  # Index of smaller element
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if array[j] <= pivot:
                i += 1 
                array[i], array[j] = array[j], array[i]      
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
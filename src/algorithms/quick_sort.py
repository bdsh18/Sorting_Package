from typing import List
from .base_sort import SortStrategy

class QuickSort(SortStrategy):
    """Implements the Quick Sort algorithm (Requirement 2)."""

    def sort(self, data: List[int], ascending: bool) -> List[int]:
        # Requirement 8: Create a copy
        arr = list(data)
        self._quick_sort_recursive(arr, 0, len(arr) - 1, ascending)
        return arr

    def _quick_sort_recursive(self, arr: List[int], low: int, high: int, ascending: bool):
        """Recursive helper function for quicksort."""
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self._partition(arr, low, high, ascending)

            # Separately sort elements before partition and after partition
            self._quick_sort_recursive(arr, low, pi - 1, ascending)
            self._quick_sort_recursive(arr, pi + 1, high, ascending)

    def _partition(self, arr: List[int], low: int, high: int, ascending: bool) -> int:
        """
        This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        array, and places all smaller (or larger) to left of
        pivot and all greater (or smaller) to right of pivot.
        """
        pivot = arr[high]  # Pivot
        i = (low - 1)      # Index of smaller/larger element

        for j in range(low, high):
            # If current element is smaller/larger than the pivot
            if (ascending and arr[j] <= pivot) or \
               (not ascending and arr[j] >= pivot):
                
                # increment index of smaller/larger element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)
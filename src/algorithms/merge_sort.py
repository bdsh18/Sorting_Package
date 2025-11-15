from typing import List
from .base_sort import SortStrategy

class MergeSort(SortStrategy):
    """Implements the Merge Sort algorithm (Requirement 2)."""

    def sort(self, data: List[int], ascending: bool) -> List[int]:
        # Requirement 8: Create a copy
        arr = list(data)
        # The recursive function will modify the copy
        self._merge_sort_recursive(arr, ascending)
        return arr

    def _merge_sort_recursive(self, arr: List[int], ascending: bool):
        """Recursive helper function for merge sort."""
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]      # Dividing the array elements
            R = arr[mid:]      # into 2 halves

            # Sort the two halves
            self._merge_sort_recursive(L, ascending)
            self._merge_sort_recursive(R, ascending)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if (ascending and L[i] < R[j]) or \
                   (not ascending and L[i] > R[j]):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
from typing import List
from .base_sort import SortStrategy

class SelectionSort(SortStrategy):
    """Implements the Selection Sort algorithm (Requirement 2)."""

    def sort(self, data: List[int], ascending: bool) -> List[int]:
        # Requirement 8: Create a copy
        arr = list(data)
        n = len(arr)

        for i in range(n):
            # Find the index of the min/max element in the remaining unsorted array
            idx_to_swap = i
            for j in range(i + 1, n):
                if (ascending and arr[j] < arr[idx_to_swap]) or \
                   (not ascending and arr[j] > arr[idx_to_swap]):
                    idx_to_swap = j
                    
            # Swap the found min/max element with the first element
            arr[i], arr[idx_to_swap] = arr[idx_to_swap], arr[i]
            
        return arr
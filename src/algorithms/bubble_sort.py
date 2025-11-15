from typing import List
from .base_sort import SortStrategy

class BubbleSort(SortStrategy):
    """Implements the Bubble Sort algorithm (Requirement 2)."""

    def sort(self, data: List[int], ascending: bool) -> List[int]:
        # Requirement 8: Create a copy to not modify the original list
        arr = list(data)
        n = len(arr)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                # Check sort condition based on 'ascending' flag
                if (ascending and arr[j] > arr[j+1]) or \
                   (not ascending and arr[j] < arr[j+1]):
                    
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            # If no two elements were swapped by inner loop, then break
            if not swapped:
                break
                
        return arr
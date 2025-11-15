"""Implementation of the Shell Sort algorithm."""
from typing import List
from .base_sort import BaseSort

class ShellSort(BaseSort):
    """Implements the Shell Sort algorithm."""
    def _sort_logic(self, array: List[int]) -> List[int]:
        """
        Sorts the array using Shell Sort (in-place).
        Args:
            array: The list of integers to sort.
        Returns:
            The sorted list.
        """
        n = len(array)
        gap = n // 2  # Start with a large gap
        # Do a gapped insertion sort for this gap size.
        while gap > 0:
            for i in range(gap, n):
                # add array[i] to the elements that have been gap sorted
                # save array[i] in temp and make a hole at position i
                temp = array[i]
                # shift earlier gap-sorted elements up until the correct
                # location for array[i] is found
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                # put temp (the original array[i]) in its correct location
                array[j] = temp
            gap //= 2  # Reduce the gap
        return array
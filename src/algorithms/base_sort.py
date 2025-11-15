"""
Abstract Base Class for Sorting Algorithms

Defines the interface that all sorting algorithms must implement.
"""
from abc import ABC, abstractmethod
from typing import List

class BaseSort(ABC):
    """Abstract base class for a sorting algorithm."""

    @abstractmethod
    def _sort_logic(self, array: List[int]) -> List[int]:
        """
        The core sorting logic. Must be implemented by subclasses.
        This method is expected to sort the list in ascending order.
        Args:
            array: The list of integers to sort.
        Returns:
            The sorted list.
        """
        raise NotImplementedError

    def sort(self, array: List[int], ascending: bool = True) -> List[int]:
        """
        Public sort method. Handles sorting direction (asc/desc).
        Args:
            array: The list of integers to sort.
            ascending: True for ascending order, False for descending.
        Returns:
            A new sorted list.
        """
        sorted_array = self._sort_logic(array)
        if ascending:
            return sorted_array
        return sorted_array[::-1] # Return reversed list for descending
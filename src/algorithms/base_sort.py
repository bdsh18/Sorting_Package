from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    """
    Abstract Base Class for all sorting algorithms.
    This defines the interface (Requirement 1).
    """
    
    @abstractmethod
    def sort(self, data: List[int], ascending: bool) -> List[int]:
        """
        Sorts a list of integers.

        Args:
            data (List[int]): The list of integers to sort.
            ascending (bool): The sort order.

        Returns:
            List[int]: A *new* list containing the sorted elements.
        """
        pass
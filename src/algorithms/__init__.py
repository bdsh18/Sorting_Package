# This file makes 'algorithms' a Python sub-package.
from .base_sort import SortStrategy
from .bubble_sort import BubbleSort
from .selection_sort import SelectionSort
from .quick_sort import QuickSort
from .merge_sort import MergeSort

__all__ = ['SortStrategy', 'BubbleSort', 'SelectionSort', 'QuickSort', 'MergeSort']
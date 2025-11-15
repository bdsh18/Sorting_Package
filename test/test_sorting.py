"""
Test suite for the Sorter class and all sorting algorithms.
(Requirement 3)
"""
import pytest
import random
# Import from 'src.sorter', as pytest is now run from the 'Sorting_Package' dir
from src.sorter import Sorter

@pytest.fixture
def sorter():
    """Provides a Sorter instance for tests."""
    return Sorter()

# Converted from a fixture to a global list for use in parametrize
TEST_CASES = [
    pytest.param([], [], id="empty"),
    pytest.param([1], [1], id="single"),
    pytest.param([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], id="pre-sorted"),
    pytest.param([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], id="reversed"),
    pytest.param([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9], id="duplicates"),
    pytest.param([-3, -1, -4, -1, -5], [-5, -4, -3, -1, -1], id="negatives"),
    pytest.param([0, 5, -10, 2, -5, 0], [-10, -5, 0, 0, 2, 5], id="mixed_with_zero"),
]

# --- UPDATE ---
# Added 'shell' to the list of algorithms to test
# ---
ALGORITHMS_TO_TEST = ["bubble", "selection", "quick", "merge", "shell"]

@pytest.mark.parametrize("algo", ALGORITHMS_TO_TEST)
@pytest.mark.parametrize("input_list, expected_sorted_asc", TEST_CASES)
def test_all_algorithms(sorter: Sorter, algo: str, input_list: list, expected_sorted_asc: list):
    """
    This single test function checks all algorithms for both ascending
    and descending order using parameterized fixtures.
    (Requirement 3)
    """
    # --- Test Ascending ---
    # Pass size_of_list=len(input_list) to satisfy our strict validation
    result_asc = sorter.sort(input_list, algo, ascending=True, size_of_list=len(input_list))
    assert result_asc == expected_sorted_asc, \
        f"{algo} sort (ascending) failed for case: {input_list}"

    # --- Test Descending ---
    # Create the expected descending list
    expected_sorted_desc = list(reversed(expected_sorted_asc))
    result_desc = sorter.sort(input_list, algo, ascending=False, size_of_list=len(input_list))
    assert result_desc == expected_sorted_desc, \
        f"{algo} sort (descending) failed for case: {input_list}"

@pytest.mark.parametrize("algo", ALGORITHMS_TO_TEST)
def test_large_random_list(sorter: Sorter, algo: str):
    """Tests algorithms on a large, randomly generated list."""
    # Using a smaller list for speed, but demonstrates the principle
    # 2e5 is too large for CI, 2000 is reasonable
    
    # Use the constants from the Sorter class
    INT32_MIN = sorter.INT32_MIN
    INT32_MAX = sorter.INT32_MAX
    
    # Use a fixed seed for reproducibility
    random.seed(42)
    large_list = [random.randint(INT32_MIN, INT32_MAX) for _ in range(2000)]
    list_size = len(large_list)
    
    # --- Test Ascending ---
    expected_asc = sorted(large_list)
    result_asc = sorter.sort(large_list, algo, ascending=True, size_of_list=list_size)
    assert result_asc == expected_asc, f"{algo} (asc) failed on large random list"
    
    # --- Test Descending ---
    expected_desc = sorted(large_list, reverse=True)
    result_desc = sorter.sort(large_list, algo, ascending=False, size_of_list=list_size)
    assert result_desc == expected_desc, f"{algo} (desc) failed on large random list"

def test_validation_errors(sorter: Sorter):
    """Tests that the Sorter class raises correct validation errors."""
    
    # Test unknown algorithm (Requirement 6b)
    with pytest.raises(ValueError, match="Unknown algorithm"):
        sorter.sort([1, 2], "magic_sort", True)
        
    # Test non-integer data (Requirement 7)
    with pytest.raises(TypeError, match="must be integers"):
        sorter.sort([1, "a", 3], "bubble", True)
        
    # Test size mismatch (Requirement 6c)
    with pytest.raises(ValueError, match="does not match the actual length"):
        sorter.sort([1, 2, 3], "bubble", True, size_of_list=4)
        
    # Test INT32 range (Requirement 5)
    INT32_MAX = sorter.INT32_MAX
    INT32_MIN = sorter.INT32_MIN
    with pytest.raises(ValueError, match="outside the allowed INT32 range"):
        sorter.sort([1, 2, INT32_MAX + 1], "bubble", True)
        
    with pytest.raises(ValueError, match="outside the allowed INT32 range"):
        sorter.sort([1, 2, INT32_MIN - 1], "selection", True)

def test_original_list_is_not_modified(sorter: Sorter):
    """Ensures the original input list is not modified (part of Requirement 8)."""
    original_list = [5, 1, 3]
    original_copy = list(original_list) # Keep a pristine copy
    
    for algo in ALGORITHMS_TO_TEST:
        sorter.sort(original_list, algo, ascending=True)
        # Check that the original list is unchanged
        assert original_list == original_copy, \
            f"{algo} sort modified the original list!"
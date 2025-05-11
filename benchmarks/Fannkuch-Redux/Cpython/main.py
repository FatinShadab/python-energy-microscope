from typing import List, Tuple


def count_flips(perm: List[int]) -> int:
    """
    Count the number of flips required to sort the given permutation.
    
    A flip reverses the section of the list that starts from the second element
    up to the position of the largest element.

    :param perm: A list of integers representing the permutation to sort.
    :return: The number of flips required to sort the permutation.
    """
    flips = 0
    perm_copy = perm.copy()
    while True:
        first = perm_copy[0]
        if first == 1:
            return flips
        perm_copy[:first] = perm_copy[:first][::-1]
        flips += 1


def next_permutation(perm: List[int]) -> bool:
    """
    Generate the next lexicographical permutation of the list.
    
    This function rearranges the list in place to the next permutation,
    returning False if the next permutation does not exist.

    :param perm: A list of integers to generate the next permutation from.
    :return: True if the next permutation exists, False if the list is in its last permutation.
    """
    n = len(perm)
    # Find the rightmost element that is smaller than the element to its right
    i = n - 2
    while i >= 0 and perm[i] > perm[i + 1]:
        i -= 1
    
    if i == -1:
        return False
    
    # Find the smallest element on the right of 'perm[i]' which is greater than 'perm[i]'
    j = n - 1
    while perm[j] < perm[i]:
        j -= 1
    
    # Swap elements at i and j
    perm[i], perm[j] = perm[j], perm[i]
    
    # Reverse the elements after position i
    perm[i + 1:] = perm[i + 1:][::-1]
    
    return True


def fannkuch_redux(n: int) -> Tuple[int, int]:
    """
    The main function to solve the Fannkuch-Redux problem.
    
    This function generates all permutations of the list [1, 2, ..., n],
    computes the number of flips required for each permutation to become sorted,
    and returns the maximum number of flips encountered along with the number
    of permutations that required that maximum number of flips.

    :param n: The number of elements in the list to permute.
    :return: A tuple (max_flips, count_max_flips) where:
             - max_flips is the maximum number of flips encountered,
             - count_max_flips is the number of permutations that required max_flips.
    """
    # Initialize the first permutation
    perm = list(range(1, n + 1))
    
    max_flips = 0
    count_max_flips = 0
    
    # We will loop over all permutations
    while True:
        flips = count_flips(perm)  # Count flips for the current permutation
        
        # Update max_flips and count_max_flips
        if flips > max_flips:
            max_flips = flips
            count_max_flips = 1
        elif flips == max_flips:
            count_max_flips += 1
        
        # Generate the next permutation
        if not next_permutation(perm):
            break
    
    return max_flips, count_max_flips


# Example usage
if __name__ == "__main__":
    n = 7  # You can change this value to test with different values of n
    max_flips, count_max_flips = fannkuch_redux(n)
    print(f"Max flips: {max_flips}")
    print(f"Count of max flips: {count_max_flips}")

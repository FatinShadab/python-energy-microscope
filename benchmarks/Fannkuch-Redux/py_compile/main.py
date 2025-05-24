from typing import List, Tuple
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


def count_flips(perm: List[int]) -> int:
    """
    Count the number of flips required to sort the given permutation.
    A flip reverses the section of the list that starts from the second element
    up to the position of the first element's value.
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
    Generate the next lexicographical permutation of the list in-place.
    Returns False if no next permutation exists (i.e., it's the last one).
    """
    n = len(perm)
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1

    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = reversed(perm[i + 1:])
    return True


def fannkuch_redux(n: int) -> Tuple[int, int]:
    """
    Solves the Fannkuch Redux problem for a given n.
    Generates all permutations of [1..n], counts flips, and tracks max.
    """
    perm = __default__["fannkuch_redux"]["perm"].copy() # 1-indexed permutation
    max_flips = 0
    count_max_flips = 0

    while True:
        flips = count_flips(perm)
        if flips > max_flips:
            max_flips = flips
            count_max_flips = 1
        elif flips == max_flips:
            count_max_flips += 1

        if not next_permutation(perm):
            break

    return max_flips, count_max_flips


def driver(n: int) -> Tuple[int, int]:
    """
    Driver function to run the fannkuch_redux logic and return results.
    """
    max_flips, count_max_flips = fannkuch_redux(n)
    print(f"Max flips: {max_flips}")
    print(f"Count of max flips: {count_max_flips}")
    return max_flips, count_max_flips


@measure_energy_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_pycompile")
def run_energy_benchmark(n: int) -> None:
    driver(n)


@measure_time_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_pycompile")
def run_time_benchmark(n: int) -> None:
    driver(n)


if __name__ == "__main__":
    n = __default__["fannkuch_redux"]["n"]
    run_energy_benchmark(n)
    run_time_benchmark(n)

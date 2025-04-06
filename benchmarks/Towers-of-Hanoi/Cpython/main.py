"""
    Towers of Hanoi - Recursive Solution

    Solving Approach:
    -----------------
    1. Move `N-1` disks from the **source** rod to the **auxiliary** rod using the **target** as a buffer.
    2. Move the `Nth` (largest) disk directly from the **source** to the **target** rod.
    3. Move the `N-1` disks from the **auxiliary** rod to the **target** rod using the **source** as a buffer.

    Rules:
    ------
    1. Only **one disk** can be moved at a time.
    2. A disk can only be placed on an **empty rod** or a **larger disk**.
    3. No disk can be placed on top of a **smaller disk**.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__
import argparse


def towers_of_hanoi(n: int, source: str, auxiliary: str, target: str) -> None:
    """
        Solves the Towers of Hanoi problem using recursion.

        Parameters:
        n (int): The number of disks to move.
        source (str): The name of the source rod.
        auxiliary (str): The name of the auxiliary rod.
        target (str): The name of the target rod.

        Returns: None
    """
    if n <= 0:
        raise ValueError("Number of disks must be a positive integer.")

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary, using target as buffer
    towers_of_hanoi(n - 1, source, target, auxiliary)
    
    # Move the nth disk to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target, using source as buffer
    towers_of_hanoi(n - 1, auxiliary, source, target)

def main(n):
    """
    Driver function to run the Towers of Hanoi problem.
    """
    try:
        towers_of_hanoi(n, "A", "B", "C")
    except ValueError as e:
        print(f"Error: {e}")

@measure_energy_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_cpython")
def run_energy_benchmark(n):
    """
    Run the energy benchmark for the Towers of Hanoi problem.
    """
    main(n)

@measure_time_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_cpython")
def run_time_benchmark(n):
    """
    Run the time benchmark for the Towers of Hanoi problem.
    """
    main(n)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Solve the Towers of Hanoi problem.")
    parser.add_argument(
        "-n", "--num_disks", type=int, default=__default__["hanoi"]["n"], 
        help=f"Number of disks (default: {__default__['hanoi']['n']})"
    )
    args = parser.parse_args()

    # Get the number of disks from the arguments or use the default value
    n = args.num_disks
    
    # Run the benchmarks
    run_energy_benchmark(n)
    run_time_benchmark(n)

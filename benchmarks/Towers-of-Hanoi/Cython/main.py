# main.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from raw import towers_of_hanoi
from input import __default__
import argparse

@measure_energy_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_cython")
def driver(n: int) -> None:
    try:
        print(f"Number of disks: {n}")
        towers_of_hanoi(n, "A", "B", "C")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Solve the Towers of Hanoi problem.")
    parser.add_argument(
        "-n", "--num_disks", type=int, default=__default__["hanoi"]["n"], 
        help=f"Number of disks (default: {__default__["hanoi"]["n"]})"
    )
    args = parser.parse_args()

    # Get the number of disks from the arguments or use the default value
    n = args.num_disks
    driver(n)
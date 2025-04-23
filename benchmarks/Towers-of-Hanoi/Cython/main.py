# main.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from raw import towers_of_hanoi
from input import __default__
import argparse


def main(n: int) -> None:
    try:
        print(f"Number of disks: {n}")
        towers_of_hanoi(n, "A", "B", "C")
    except ValueError as e:
        print(f"Error: {e}")
        
@measure_energy_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_cython")
def run_energy_benchmark(n: int) -> None:
    """
    Driver function to run the Towers of Hanoi solution and measure energy consumption.
    
    Args:
        n (int): Number of disks.
    """
    main(n)

@measure_time_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_cython")
def run_time_benchmark(n: int) -> None:
    """
    Driver function to run the Towers of Hanoi solution and measure time consumption.
    
    Args:
        n (int): Number of disks.
    """
    main(n)


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
    
    run_energy_benchmark(n)
    run_time_benchmark(n)

# main.py
import numpy as np
from raw import Body, simulate_nbody
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


def print_trajectories(positions: List[List[List[float]]], num_bodies: int) -> None:
    """
    Prints the positions of each body at each time step.

    Args:
        positions (List[List[List[float]]]): A list of positions for each body at each time step.
        num_bodies (int): The number of bodies in the simulation.
    """
    for body_index in range(num_bodies):
        print(f"Trajectory of Body {body_index + 1}:")
        for step, position in enumerate(positions):
            pos = position[body_index]
            print(f"Step {step + 1}: Position = {pos}")
        print()

def driver(bodies: List[Body], dt: float, num_steps: int) -> None:
    """
    Initializes the bodies, runs the N-Body simulation, and prints the results.
    """
    positions = simulate_nbody(bodies, dt, num_steps)
    print_trajectories(positions, len(bodies))

@measure_time_to_csv(n=__default__["nbody"]["test_n"], csv_filename="nbody_cython")
def run_time_benchmark(bodies: List[Body], dt: float, num_steps: int) -> None:
    """
    Runs the N-Body simulation and measures the time taken.
    """
    driver(bodies, dt, num_steps)

@measure_energy_to_csv(n=__default__["nbody"]["test_n"], csv_filename="nbody_cython")
def run_energy_benchmark(bodies: List[Body], dt: float, num_steps: int) -> None:
    """
    Runs the N-Body simulation and measures the energy consumed.
    """
    driver(bodies, dt, num_steps)


if __name__ == "__main__":
    bodies = [
        Body(
            body["mass"],
            np.array(body["position"], dtype=np.float64),
            np.array(body["velocity"], dtype=np.float64)
        )
        for body in __default__["nbody"]["bodies"]
    ]

    dt = __default__["nbody"]["dt"]
    num_steps = __default__["nbody"]["time_steps"]

    # Run the energy benchmark
    run_energy_benchmark(bodies, dt, num_steps)
    run_time_benchmark(bodies, dt, num_steps)

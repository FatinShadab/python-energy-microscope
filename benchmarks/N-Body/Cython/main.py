# main.py
import numpy as np
from raw import Body, simulate_nbody
from typing import List

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

def main():
    body1 = Body(5.972e24, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
    body2 = Body(7.348e22, np.array([384400000.0, 0.0, 0.0]), np.array([0.0, 1022.0, 0.0]))
    
    bodies = [body1, body2]

    dt = 1000
    num_steps = 10000
    positions = simulate_nbody([body1, body2], dt, num_steps)
    
    print_trajectories(positions, len(bodies))

if __name__ == "__main__":
    main()

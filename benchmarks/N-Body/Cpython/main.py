import math
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


# Constants
G = __default__["nbody"]["G"]  # Gravitational constant (m^3 kg^-1 s^-2)

class Body:
    """
    A class to represent a celestial body in the N-Body simulation.
    
    Attributes:
        mass (float): Mass of the body (in kg).
        position (List[float]): Position of the body (in meters, as a 3D vector).
        velocity (List[float]): Velocity of the body (in meters per second, as a 3D vector).
    
    Methods:
        update_position(dt: float) -> None:
            Updates the position of the body based on its velocity and the time step.
        
        update_velocity(force: List[float], dt: float) -> None:
            Updates the velocity of the body based on the net force and the time step.
    """
    def __init__(self, mass: float, position: List[float], velocity: List[float]) -> None:
        """
        Initializes the Body object with mass, position, and velocity.

        Args:
            mass (float): Mass of the body in kg.
            position (List[float]): Initial position as a 3D vector.
            velocity (List[float]): Initial velocity as a 3D vector.
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity  # No need for NumPy, just use a normal list.

    def update_position(self, dt: float) -> None:
        """
        Updates the position of the body using the formula: position += velocity * dt.

        Args:
            dt (float): The time step (in seconds) used to update the position.
        """
        self.position = [p + v * dt for p, v in zip(self.position, self.velocity)]

    def update_velocity(self, force: List[float], dt: float) -> None:
        """
        Updates the velocity of the body using the formula: velocity += force / mass * dt.

        Args:
            force (List[float]): The gravitational force acting on the body.
            dt (float): The time step (in seconds) used to update the velocity.
        """
        self.velocity = [v + f / self.mass * dt for v, f in zip(self.velocity, force)]


def compute_gravitational_force(body1: Body, body2: Body) -> List[float]:
    """
    Computes the gravitational force between two bodies.

    Args:
        body1 (Body): The first body.
        body2 (Body): The second body.

    Returns:
        List[float]: The gravitational force vector (in Newtons) acting on body1 due to body2.
    """
    # Compute the distance between the two bodies
    distance = math.sqrt(sum((b1 - b2) ** 2 for b1, b2 in zip(body1.position, body2.position)))

    if distance == 0:
        return [0.0, 0.0, 0.0]  # Avoid division by zero if the bodies overlap

    force_magnitude = G * body1.mass * body2.mass / distance ** 2

    # Compute the direction vector
    direction = [(b2 - b1) / distance for b1, b2 in zip(body1.position, body2.position)]

    # Calculate the force vector
    force = [force_magnitude * d for d in direction]
    return force


def simulate_nbody(bodies: List[Body], dt: float, num_steps: int) -> List[List[List[float]]]:
    """
    Simulates the motion of N bodies under mutual gravitational attraction using Euler's method.

    Args:
        bodies (List[Body]): A list of Body objects representing the celestial bodies in the system.
        dt (float): The time step (in seconds) for the simulation.
        num_steps (int): The number of steps to simulate.

    Returns:
        List[List[List[float]]]: A list of positions for each body at each time step.
    """
    positions = []

    for step in range(num_steps):
        # Store the positions of each body at this time step
        positions.append([body.position[:] for body in bodies])

        # Calculate the forces and update velocities and positions
        forces = [[0.0, 0.0, 0.0] for _ in bodies]  # Initialize forces as zero vectors

        # Calculate forces between each pair of bodies
        for i, body1 in enumerate(bodies):
            for j, body2 in enumerate(bodies):
                if i != j:
                    force = compute_gravitational_force(body1, body2)
                    forces[i] = [f + new_f for f, new_f in zip(forces[i], force)]

        # Update velocities and positions of bodies
        for i, body in enumerate(bodies):
            body.update_velocity(forces[i], dt)
            body.update_position(dt)

    return positions


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

def driver(boides: List[Body], dt: float, num_steps: int) -> None:
    """
        Initializes the bodies, runs the N-Body simulation, and prints the results.
    """
    # Run the simulation
    positions = simulate_nbody(bodies, dt, num_steps)
    
    # Output the results
    print_trajectories(positions, len(bodies))
    
@measure_time_to_csv(n=__default__["nbody"]["test_n"], csv_filename="nbody_cpython")
def run_time_benchmark(boides: List[Body], dt: float, num_steps: int) -> None:
    """
    Runs the N-Body simulation and measures the time taken.
    """
    driver(boides, dt, num_steps)

@measure_energy_to_csv(n=__default__["nbody"]["test_n"], csv_filename="nbody_cpython")
def run_energy_benchmark(bodies: List[Body], dt: float, num_steps: int) -> None:
    """
    Runs the N-Body simulation and measures the energy consumed.
    """
    driver(bodies, dt, num_steps)


if __name__ == "__main__":
    bodies = [
        Body(body["mass"], body["position"], body["velocity"])
        for body in __default__["nbody"]["bodies"]
    ]

    # Run the simulation
    dt = __default__["nbody"]["dt"]
    num_steps = __default__["nbody"]["time_steps"]

    # Run the energy benchmark
    run_energy_benchmark(bodies, dt, num_steps)
    # Run the time benchmark
    run_time_benchmark(bodies, dt, num_steps)

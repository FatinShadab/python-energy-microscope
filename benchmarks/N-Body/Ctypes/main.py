import ctypes
import numpy as np
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


# Load the compiled shared library
lib = ctypes.CDLL('./libnbody.so')  # or 'nbody.dll' on Windows

# Define the Body structure
class Body(ctypes.Structure):
    _fields_ = [
        ("mass", ctypes.c_double),
        ("position", ctypes.c_double * 3),
        ("velocity", ctypes.c_double * 3)
    ]

# Define the simulate_nbody function signature
lib.simulate_nbody.argtypes = [
    ctypes.POINTER(Body), ctypes.c_int,
    ctypes.c_double, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double)
]
lib.simulate_nbody.restype = None

def run_simulation(bodies: List[Body], dt: float, num_steps: int) -> List[List[List[float]]]:
    num_bodies = len(bodies)
    body_array = (Body * num_bodies)(*bodies)

    # Allocate output buffer
    output = (ctypes.c_double * (num_steps * num_bodies * 3))()

    # Call C function
    lib.simulate_nbody(body_array, num_bodies, dt, num_steps, output)

    # Convert output to nested Python lists
    results = []
    for step in range(num_steps):
        step_positions = []
        for i in range(num_bodies):
            index = step * num_bodies * 3 + i * 3
            step_positions.append([output[index], output[index + 1], output[index + 2]])
        results.append(step_positions)

    return results

def main():
    body1 = Body(5.972e24, (0, 0, 0), (0, 0, 0))
    body2 = Body(7.348e22, (384400000, 0, 0), (0, 1022, 0))

    dt = 1000
    num_steps = 10000
    results = run_simulation([body1, body2], dt, num_steps)

    for i, traj in enumerate(zip(*results)):
        print(f"Trajectory of Body {i+1}:")
        for step, pos in enumerate(traj):
            print(f"Step {step + 1}: Position = {pos}")
        print()

if __name__ == "__main__":
    main()

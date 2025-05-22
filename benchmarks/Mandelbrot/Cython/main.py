# main.py
from raw import generate_mandelbrot
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


def render_mandelbrot(data, max_iter):
    chars = " .:-=+*#%@"
    scale = len(chars) - 1

    for row in data:
        print("".join(chars[int(i / max_iter * scale)] for i in row))
        
def driver(width: int, height: int, max_iter: int, 
                         x_min: float, x_max: float, y_min: float, y_max: float):
    data = generate_mandelbrot(width, height, max_iter, x_min, x_max, y_min, y_max)
    render_mandelbrot(data, max_iter)

# Measure energy consumption and time taken for the Mandelbrot set generation
@measure_energy_to_csv(n=__default__["mandelbrot"]["test_n"], csv_filename="mandelbrot_cython")
def run_energy_benchmark(width: int, height: int, max_iter: int, 
                         x_min: float, x_max: float, y_min: float, y_max: float) -> None:
    driver(width, height, max_iter, x_min, x_max, y_min, y_max)

# Measure time taken for the Mandelbrot set generation
@measure_time_to_csv(n=__default__["mandelbrot"]["test_n"], csv_filename="mandelbrot_cython")
def run_time_benchmark(width: int, height: int, max_iter: int, 
                         x_min: float, x_max: float, y_min: float, y_max: float) -> None:
    driver(width, height, max_iter, x_min, x_max, y_min, y_max)
    

if __name__ == "__main__":
    width, height = __default__["mandelbrot"]["width"], __default__["mandelbrot"]["height"]
    max_iter = __default__["mandelbrot"]["max_iter"]  # Maximum iterations per point
    x_min, x_max, y_min, y_max = (
        __default__["mandelbrot"]["x_min"],
        __default__["mandelbrot"]["x_max"],
        __default__["mandelbrot"]["y_min"],
        __default__["mandelbrot"]["y_max"]
    )

    # Run energy and time benchmarks
    run_energy_benchmark(width, height, max_iter, x_min, x_max, y_min, y_max)
    run_time_benchmark(width, height, max_iter, x_min, x_max, y_min, y_max)

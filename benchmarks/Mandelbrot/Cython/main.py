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
        
def main():
    width, height = 80, 40
    max_iter = 100
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5

    data = generate_mandelbrot(width, height, max_iter, x_min, x_max, y_min, y_max)
    render_mandelbrot(data, max_iter)

if __name__ == "__main__":
    main()

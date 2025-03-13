import sys

def mandelbrot(c: complex, max_iter: int) -> int:
    """
    Determines if a given complex number `c` belongs to the Mandelbrot set.
    
    The function iterates the equation:
        Z(n+1) = Z(n)^2 + C
    where Z starts at 0. If |Z| exceeds 2 before `max_iter` iterations, 
    the point escapes and the iteration count is returned. Otherwise, 
    max_iter is returned indicating the point is inside the set.

    Args:
        c (complex): The complex number to check.
        max_iter (int): The maximum number of iterations to check before assuming containment.

    Returns:
        int: The number of iterations before escape (or max_iter if it does not escape).
    """
    z: complex = 0 + 0j  # Start with Z = 0
    for i in range(max_iter):
        z = z * z + c  # Apply Mandelbrot iteration
        if abs(z) > 2:  # If magnitude exceeds 2, it escapes
            return i
    return max_iter  # If max_iter is reached, assume it's inside the set

def generate_mandelbrot(width: int, height: int, max_iter: int, 
                         x_min: float, x_max: float, y_min: float, y_max: float) -> list[list[int]]:
    """
    Generates a Mandelbrot set representation as a 2D list of iteration counts.
    
    Each pixel maps to a complex number (C) in the given range, and the Mandelbrot 
    function is applied to determine its escape time.

    Args:
        width (int): The width of the output grid.
        height (int): The height of the output grid.
        max_iter (int): The maximum iterations for Mandelbrot calculation.
        x_min (float): Minimum x-coordinate (real part).
        x_max (float): Maximum x-coordinate (real part).
        y_min (float): Minimum y-coordinate (imaginary part).
        y_max (float): Maximum y-coordinate (imaginary part).

    Returns:
        list[list[int]]: A 2D list containing iteration counts for each point.
    """
    aspect_ratio: float = width / height  # Adjust the Y range for aspect ratio
    y_min, y_max = y_min / aspect_ratio, y_max / aspect_ratio
    mandelbrot_set: list[list[int]] = []  # 2D list to store iteration counts

    for y in range(height):
        row: list[int] = []  # Store iteration values for a row
        for x in range(width):
            real: float = x_min + (x / width) * (x_max - x_min)  # Map pixel x to real part
            imag: float = y_min + (y / height) * (y_max - y_min)  # Map pixel y to imaginary part
            c: complex = complex(real, imag)  # Construct complex number
            row.append(mandelbrot(c, max_iter))  # Compute Mandelbrot iteration count
        mandelbrot_set.append(row)
    
    return mandelbrot_set  # Return 2D list of iteration counts

def render_mandelbrot(data: list[list[int]], max_iter: int) -> None:
    """
    Renders the Mandelbrot set using ASCII characters.
    
    The ASCII characters provide a visual representation of iteration depth.
    Darker characters represent higher iteration counts (points inside the set).

    Args:
        data (list[list[int]]): The Mandelbrot set iteration values.
        max_iter (int): Maximum iteration count used for normalization.
    
    Returns:
        None: Prints the ASCII visualization to the terminal.
    """
    chars: str = " .:-=+*#%@"
    scale: int = len(chars) - 1  # Scale factor for character selection

    for row in data:
        print("".join(chars[int(i / max_iter * scale)] for i in row))  # Map values to ASCII chars

if __name__ == "__main__":
    # Define grid size and Mandelbrot range
    width, height = 80, 40  # Output size in characters
    max_iter = 100  # Maximum iterations per point
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5  # Mandelbrot coordinate range

    # Generate Mandelbrot data
    mandelbrot_data = generate_mandelbrot(width, height, max_iter, x_min, x_max, y_min, y_max)

    # Render Mandelbrot fractal as ASCII
    render_mandelbrot(mandelbrot_data, max_iter)

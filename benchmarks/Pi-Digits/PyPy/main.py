import math

def compute_pi_gauss_legendre(iterations: int = 10) -> float:
    """
    Computes an approximation of Pi using the Gauss-Legendre algorithm.

    This algorithm iteratively refines the value of Pi with quadratic convergence,
    meaning the number of correct digits roughly doubles in each iteration.

    Parameters:
    iterations (int): The number of iterations to perform. More iterations yield higher precision.

    Returns:
    float: The computed value of Pi.
    """
    # Initialize variables
    a: float = 1.0
    b: float = 1.0 / math.sqrt(2)
    t: float = 0.25
    p: float = 1.0

    for _ in range(iterations):
        a_next: float = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2  # Double p in each iteration

    # Compute final Pi approximation
    return ((a + b) ** 2) / (4 * t)


if __name__ == "__main__":
    ITERATIONS = 20  # Adjust for precision
    pi_approx: float = compute_pi_gauss_legendre(ITERATIONS)

    print(f"Computed Pi: {pi_approx}")

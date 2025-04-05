import timeit

import raw  # Import the compiled Cython module

def test():
    # Test the `main` function with a specific depth
    n = 20  # Example depth value
    raw.main(n)  # Call the Cython function

if __name__ == "__main__":
    runtime = timeit.timeit("test()", globals=globals(), number=1)
    print(f"Runtime: {runtime} seconds")

import raw  # Import the compiled Cython module

def test():
    # Test the `main` function with a specific depth
    n = 6  # Example depth value
    raw.main(n)  # Call the Cython function

if __name__ == "__main__":
    test()

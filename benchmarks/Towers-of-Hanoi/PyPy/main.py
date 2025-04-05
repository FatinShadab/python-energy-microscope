"""
    Towers of Hanoi - Recursive Solution

    Solving Approach:
    -----------------
    1. Move `N-1` disks from the **source** rod to the **auxiliary** rod using the **target** as a buffer.
    2. Move the `Nth` (largest) disk directly from the **source** to the **target** rod.
    3. Move the `N-1` disks from the **auxiliary** rod to the **target** rod using the **source** as a buffer.

    Rules:
    ------
    1. Only **one disk** can be moved at a time.
    2. A disk can only be placed on an **empty rod** or a **larger disk**.
    3. No disk can be placed on top of a **smaller disk**.
"""

def towers_of_hanoi(n: int, source: str, auxiliary: str, target: str) -> None:
    """
        Solves the Towers of Hanoi problem using recursion.

        Parameters:
        n (int): The number of disks to move.
        source (str): The name of the source rod.
        auxiliary (str): The name of the auxiliary rod.
        target (str): The name of the target rod.

        Returns: None
    """
    if n <= 0:
        raise ValueError("Number of disks must be a positive integer.")

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary, using target as buffer
    towers_of_hanoi(n - 1, source, target, auxiliary)
    
    # Move the nth disk to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target, using source as buffer
    towers_of_hanoi(n - 1, auxiliary, source, target)


if __name__ == "__main__":
    try:
        n = 3  # Number of disks
        towers_of_hanoi(n, "A", "B", "C")
    except ValueError as e:
        print(f"Error: {e}")

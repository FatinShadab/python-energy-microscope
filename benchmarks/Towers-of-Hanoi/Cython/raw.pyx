# raw.pyx -> hanoi

def towers_of_hanoi(int n, str source, str auxiliary, str target):
    """
    Solves the Towers of Hanoi problem using recursion.

    Parameters:
        n (int): The number of disks to move.
        source (str): The name of the source rod.
        auxiliary (str): The name of the auxiliary rod.
        target (str): The name of the target rod.
    """
    if n <= 0:
        raise ValueError("Number of disks must be a positive integer.")

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    towers_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, source, target)

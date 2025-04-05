# main.py

from raw import towers_of_hanoi

if __name__ == "__main__":
    try:
        n = 10
        print(f"Number of disks: {n}")
        towers_of_hanoi(n, "A", "B", "C")
    except ValueError as e:
        print(f"Error: {e}")

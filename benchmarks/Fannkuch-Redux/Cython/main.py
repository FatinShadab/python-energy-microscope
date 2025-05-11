from raw import fannkuch_redux

def main():
    n = 7
    max_flips, count_max_flips = fannkuch_redux(n)
    print(f"Max flips: {max_flips}")
    print(f"Count of max flips: {count_max_flips}")
    
    
if __name__ == "__main__":
    main()

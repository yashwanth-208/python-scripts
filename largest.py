import sys

def find_largest_number(numbers):
    return max(numbers)

def main():
    numbers = list(map(int, sys.stdin.read().strip().split()))  # Read input from standard input
    largest_number = find_largest_number(numbers)
    print(Largest number:, largest_number)

if __name__ == __main__:
    main()

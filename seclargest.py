import sys

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else None

def main():
    numbers = list(map(int, sys.stdin.read().strip().split()))  # Read input from standard input
    second_largest = find_second_largest(numbers)
    print(Second largest number:, second_largest)

if __name__ == __main__:
    main()

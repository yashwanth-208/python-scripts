def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(text):
    palindromes = set()
    length = len(text)
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = text[i:j]
            if is_palindrome(substring) and len(substring) > 1:
                palindromes.add(substring)
    
    return palindromes

import sys

def main():
    text = sys.stdin.read().strip()  # Read input from standard input
    palindrome_list = find_palindromes(text)
    print(Palindromic substrings:, palindrome_list)

if __name__ == __main__:
    main()

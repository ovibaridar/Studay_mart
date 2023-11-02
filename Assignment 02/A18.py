def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

n = input("Enter a string: ")
print(is_palindrome(n))
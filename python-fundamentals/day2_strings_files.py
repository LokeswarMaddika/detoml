# Day 2 - Functions, File Handling, String Problems

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

# Error handling
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Please provide numbers only"

# File handling
with open("test.txt", "w") as f:
    f.write("Hello Lokesh\n")
    f.write("Day 2 of Python\n")

with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# LeetCode 344 - Reverse String
def reverseString(s):
    s[:] = s[::-1]

# LeetCode 242 - Valid Anagram
def isAnagram(s, t):
    cnt_s = {}
    cnt_t = {}
    for char in s:
        if char in cnt_s:
            cnt_s[char] += 1
        else:
            cnt_s[char] = 1
    for char in t:
        if char in cnt_t:
            cnt_t[char] += 1
        else:
            cnt_t[char] = 1
    return cnt_s == cnt_t

# LeetCode 20 - Valid Parentheses
def isValid(s):
    stack = []
    matches = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != matches[char]:
                return False
    return len(stack) == 0
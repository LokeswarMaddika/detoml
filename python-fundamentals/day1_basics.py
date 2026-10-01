lokeshmaddika@Lokeswars-MacBook-Pro ~ % python3                        
Python 3.9.6 (default, Aug 25 2026, 21:26:21) 
[Clang 21.0.0 (clang-2100.3.34.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Day 1 - Back on tracl')
Day 1 - Back on tracl
>>> print('Day 1 - Back on track')
Day 1 - Back on track
>>> name = 'Lokesh'
>>> age = 28
>>> height = 5.11
>>> is_engineer = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> is_engineer = True
>>> print(name)
Lokesh
>>> print(age)
28
>>> print(height)
5.11
>>> print(is_engineer)
True
>>> print(type(name))
<class 'str'>
>>> print(type(age))
<class 'int'>
>>> print(type(height))
<class 'float'>
>>> print(type(is_engineer))
<class 'bool'>
>>> x=10
>>> y=3
>>> print(x + y)   # addition
13
>>> print(x - y)   # subtraction
7
>>> print(x * y)   # multiplication
30
>>> print(x / y)   # division
3.3333333333333335
>>> print(x // y)  # floor division (no decimal)
3
>>> print(x % y)   # modulo (remainder)
1
>>> print(x ** y)  # power
1000
>>> first = "Lokesh"
>>> last = "Maddika"
>>> # Concatenation
>>> full_name = first + " " + last
>>> print(full_name)
Lokesh Maddika
>>> # Length
>>> print(len(full_name))
14
>>> # Uppercase and lowercase
>>> print(full_name.upper())
LOKESH MADDIKA
>>> print(full_name.lower())
lokesh maddika
>>> 
>>> # Indexing - get a single character
>>> print(full_name[0])  # first character
L
>>> print(full_name[-1]) # last character
a
>>> print(full_name[0:6])  
Lokesh
>>> print(full_name[7:]) 
Maddika
>>> print(full_name[:6])  
Lokesh
>>> numbers = [1, 2, 3, 4, 5]
>>> mixed = [1, "hello", True, 3.14]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> print(mixed)
[1, 'hello', True, 3.14]
>>> print(numbers[0])    # first element
1
>>> print(numbers[-1])   # last element
5
>>> print(len(numbers))  # length
5
>>> 
>>> # Adding and removing
>>> numbers.append(6)    # add to end
>>> print(numbers)
[1, 2, 3, 4, 5, 6]
>>> 
>>> numbers.remove(3)    # remove value 3
>>> print(numbers)
[1, 2, 4, 5, 6]
>>> numbers = [1, 2, 3, 4, 5]
>>> 
>>> # Loop through each element
>>> for num in numbers:
...     print(num)
... 
1
2
3
4
5
>>> # Print only even numbers
>>> for num in numbers:
...     if num % 2 == 0:
...         print(num)
... 
2
4
>>> def sum_of_evens(numsbers):
... for num in nums:
  File "<stdin>", line 2
    for num in nums:
    ^
IndentationError: expected an indented block
>>> 
>>> 
>>> def sum_of_evens(numsbers):
...     for num in nums:
...             if num % 2 == 0
  File "<stdin>", line 3
    if num % 2 == 0
                   ^
SyntaxError: invalid syntax
>>> def sum_of_evens(numsbers):
...     for num in nums:
...             if num % 2 == 0:
...                     total += sum
... 
>>> 
>>> def sum_of_evens(numsbers):
... sum = 0
  File "<stdin>", line 2
    sum = 0
    ^
IndentationError: expected an indented block
>>> def sum_of_evens(numsbers):
...     sum = 0
...     for num in nums:
...             if num % 2 == 0:
...                     total += sum
...     return total
... 
>>> result = sum_of_evens([1,2,3,4,5,6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sum_of_evens
NameError: name 'nums' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def sum_of_evens(numsbers):
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> 
>>> 
>>> 
>>> def sum_of_evens(numbers):
...     sum = 0
...     for num in nums:
...             if num % 2 == 0:
...                     sum += num
...     return sum
... 
>>> result = sum_of_evens([1,2,3,4,5,6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sum_of_evens
NameError: name 'nums' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def sum_of_evens(numbers):
... total = 0
  File "<stdin>", line 2
    total = 0
    ^
IndentationError: expected an indented block
>>> 
>>> 
>>> 
>>> def sum_of_evens(numbers):
...     total = 0
...     for i in numbers:
...             if i % 2 == 0:
...                     total += i
...     return total
... 
>>> result = sum_of_evens([1,2,3,4,5,6])
>>> print(result)
12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def count_vowels(text):
...     cnt = 0
...     for i in text:
...             if i in 
  File "<stdin>", line 4
    if i in 
            ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> def count_vowels(text):
...     cnt = 0
...     vowels = [a,e,i,o,u]
...     for i in text:
...             if i in vowels:
...                     cnt += 1
...     return cnt
... 
>>> result = count_vowels('Lokesh')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in count_vowels
NameError: name 'a' is not defined
>>> 
>>> 
>>> 
>>> def count_vowels(text):
...     cnt = 0
...     vowels = ['a','e','i','o','u']
...     for i in text:
...             if i in vowels:
...                     cnt += 1
...     return cnt
... 
>>> result = count_vowels('Lokesh')
>>> print(result)
2
>>> person = {
...     "name": "Lokesh",
...     "age": 28,
...     "role": "Data Engineer"
... }
>>> 
>>> print(person)
{'name': 'Lokesh', 'age': 28, 'role': 'Data Engineer'}
>>> print(person["name"])    # access by key
Lokesh
>>> print(person["role"])    # access by key
Data Engineer
>>> 
>>> 
>>> print(person['name'])
Lokesh
>>> print(person[name])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Lokesh'
>>> # Add new key
>>> person["city"] = "Atlanta"
>>> print(person)
{'name': 'Lokesh', 'age': 28, 'role': 'Data Engineer', 'city': 'Atlanta'}
>>> 
>>> # Update existing key
>>> person["age"] = 29
>>> print(person["age"])
29
>>> 
>>> # Delete a key
>>> del person["city"]
>>> print(person)
{'name': 'Lokesh', 'age': 29, 'role': 'Data Engineer'}
>>> 
>>> # Check if key exists
>>> print("name" in person)
True
>>> print("salary" in person)
False
>>> 
>>> 
>>> 
>>> # Loop through keys
>>> for key in person:
...     print(key)
... 
name
age
role
>>> # Loop through keys and values together
>>> for key, value in person.items():
...     print(f"{key}: {value}")
... 
name: Lokesh
age: 29
role: Data Engineer
>>> 
>>> print(key + ": " + value)  # messy concatenation
role: Data Engineer
>>> print(f"{key}: {value}")  # clean, readable
role: Data Engineer
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     cnt = 0
...
... 
>>> 
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     counts = {}
...     words = sentence.split()
  File "<stdin>", line 3
    words = sentence.split()
                            ^
IndentationError: unindent does not match any outer indentation level
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     counts = {}
...     words = sentence.split()
...     for i in words:
...             if i in counts:
...                     counts += 1
...             else:
...                     counts = 1
...     return counts
... 
>>> result = word_count('the cat sat on the mat')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in word_count
TypeError: argument of type 'int' is not iterable
>>> result = word_count("the cat sat on the mat")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in word_count
TypeError: argument of type 'int' is not iterable
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     cnt = {}
...     words = sentence.split()
...     for i in words:
...             if i in cnt:
...                     cnt[word] += 1
...             else:
...                     cnt
... 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     cnt = {}
...     words = sentence.split()
...     for i in words:
...             if i in cnt:
...                     cnt[i] += 1
... 
>>> 
>>> 
>>> 
>>> def word_count(sentence):
...     cnt = {}
...     words = sentence.split()
...     for i in words:
...             if i in cnt:
...                     cnt[i] += 1
...             else:
...                     cnt[i] = 1
...     return cnt
... 
>>> result = word_count("the cat sat on the mat")
>>> print(result)
{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> 
>>> # Normal loop to get even numbers
>>> evens = []
>>> for num in numbers:
...     if num % 2 == 0:
...         evens.append(num)
... 
>>> # Same thing with list comprehension - one line
>>> evens = [num for num in numbers if num % 2 == 0]
>>> 
>>> print(evens)
[2, 4, 6]
>>> 
>>> 
>>> 
>>> squares = [num ** 2 for num in range(1,11)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> 
>>> 
>>> 
>>> coordinates = (10, 20)
>>> print(coordinates)
(10, 20)
>>> print(coordinates[0])
10
>>> print(coordinates[1])
20
>>> 
>>> # Try to change a value
>>> coordinates[0] = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers = [1, 2, 2, 3, 3, 3, 4]
>>> unique = set(numbers)
>>> print(unique)
{1, 2, 3, 4}
>>> 
>>> # Set operations
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> 
>>> print(a & b)  # intersection - common elements
{3, 4}
>>> print(a | b)  # union - all elements
{1, 2, 3, 4, 5, 6}
>>> print(a - b)  # difference - in a but not b
{1, 2}
>>> 
>>> 
>>> \\
  File "<stdin>", line 1
    \\
     ^
SyntaxError: unexpected character after line continuation character
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def has_duplicates(nums):
...     return len(nums) != len(set(nums))
... 
>>> result = has_duplicates([1,2,3,4])
>>> print(result)
False
>>> result = has_duplicates([1,2,2,3,3,4])
>>> print(result)
True
>>> nums = [1,2,2,3,3,4,5,5,6]
>>> print(set(nums))
{1, 2, 3, 4, 5, 6}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def is_palindrome(text):
...     word = text
...     if i in word:
...             word[i] = word[n-1]
...
... 
>>> 
>>> 
>>> def is_palindrome(text):
...     if text == text[::-1]:
...             return True
...     else:
...             return False
... 
>>> result = is_palindrome("hello")
>>> print(result)
False
>>> result = is_palindrome("racecar")
>>> print(result)
True
>>> result = is_palindrome("murder")
>>> print(result)
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def is_palindrome_num(n):
...     return str(n) == str(n)[::-1]
... 
>>> print(is_palindrome_num(121))   # True
True
>>> print(is_palindrome_num(123))   # False
False
>>> print(is_palindrome_num(1221))  # True
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> exit()

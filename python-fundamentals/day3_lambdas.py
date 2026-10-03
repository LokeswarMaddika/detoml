lokeshmaddika@Lokeswars-MacBook-Pro detoml % 
lokeshmaddika@Lokeswars-MacBook-Pro detoml % python3
Python 3.9.6 (default, Aug 25 2026, 21:26:21) 
[Clang 21.0.0 (clang-2100.3.34.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> 
>>> 
>>> def square(x):
...     return x**2
... 
>>> print(square(5))
25
>>> 
>>> 
>>> 
>>> 
>>> square = lambda x: x**2
>>> print(square(10))
100
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers = [1,2,3,4,5]
>>> squared = list(map(lambda x:x**2, numbers))
>>> print(squared)
[1, 4, 9, 16, 25]
>>> evens = list(filter(lambda x: x%2 == 0, numbers))
>>> print(evens)
[2, 4]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> squared = list(map(lambda x: x**2, numbers))
>>> squared = [x**2 for x in numbers]
>>> 
>>> print(squared)
[1, 4, 9, 16, 25]
>>> squared = list(map(lambda x: x**2, numbers))
>>> print(squared)
[1, 4, 9, 16, 25]
>>> squared = [x**2 for x in numbers]
>>> print(squared)
[1, 4, 9, 16, 25]
>>> 
>>> 
>>> 
>>> 
>>> evens = list(map(lambda x:x%2 == 0, numbers))
>>> print(evens)
[False, True, False, True, False]
>>> evens = list(filter(lambda x:x%2 == 0, numbers))
>>> print(evens)
[2, 4]
>>> evens = [x for x in numbers if x%2 == 0]
>>> print(evens)
[2, 4]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> /*True*/
  File "<stdin>", line 1
    /*True*/
    ^
SyntaxError: invalid syntax
>>> //True
  File "<stdin>", line 1
    //True
    ^
SyntaxError: invalid syntax
>>> --True
1
>>> """
... gtrye
... """
'\ngtrye\n'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> """
... map vs filter:
... 
... map — transforms every element, same number of elements out as in
... filter — keeps only elements where condition is True, fewer elements out
... 
... 
... 
... List comprehension is more Pythonic and readable — use that in interviews. Lambda with map/filter you'll see in existing codebases and pandas, so worth knowing.
... 
... 
... 
... """
"\nmap vs filter:\n\nmap — transforms every element, same number of elements out as in\nfilter — keeps only elements where condition is True, fewer elements out\n\n\n\nList comprehension is more Pythonic and readable — use that in interviews. Lambda with map/filter you'll see in existing codebases and pandas, so worth knowing.\n\n\n\n"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> students = [
...     {:name": "Alice", "grade": 85},
  File "<stdin>", line 2
    {:name": "Alice", "grade": 85},
     ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> students = {
... 
... 
... 
... 
... }
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> students = [
...     {"name": "Alice", "grade": 85},
...     {"name": "Bob", "grade": 92},
...     {"name": "Charlie", "grade": 78}
... ]
>>> 
>>> 
>>> 
>>> sorted_students = sorted(students, key = lambda x: x["grade"])
>>> for s in sorted_students:
...     print(s)
... 
{'name': 'Charlie', 'grade': 78}
{'name': 'Alice', 'grade': 85}
{'name': 'Bob', 'grade': 92}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> sorted_students = sorted(students, key = lambda x: x["grade"], reverse=True)
>>> for s in sorted_students:
...     print(s)
... 
{'name': 'Bob', 'grade': 92}
{'name': 'Alice', 'grade': 85}
{'name': 'Charlie', 'grade': 78}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> """
... key parameter in sorted():
... 
... key tells Python what to sort by. Without it, Python doesn't know which part of a complex object to use for comparison.
... """
"\nkey parameter in sorted():\n\nkey tells Python what to sort by. Without it, Python doesn't know which part of a complex object to use for comparison.\n"
>>> 
>>> 
>>> 
>>> 
>>> """
... ach student is a dictionary {"name": "Alice", "grade": 85}. Python can't automatically know whether to sort by name or grade — you have to specify.
... 
... key=lambda x: x["grade"] means: "for each item x, extract x["grade"] and use that value for sorting."
... 
... Simple analogy:
... Imagine sorting a pile of envelopes. key tells Python: sort by the number written on the front, not by the size of the envelope or the name on it."""
'\nach student is a dictionary {"name": "Alice", "grade": 85}. Python can\'t automatically know whether to sort by name or grade — you have to specify.\n\nkey=lambda x: x["grade"] means: "for each item x, extract x["grade"] and use that value for sorting."\n\nSimple analogy:\nImagine sorting a pile of envelopes. key tells Python: sort by the number written on the front, not by the size of the envelope or the name on it.'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> words = ["banana", "apple", "kiwi", "mango"]
>>> sorted(words, key = lambda x: len(x))
['kiwi', 'apple', 'mango', 'banana']
>>> 
>>> 
>>> sorted(words, key = lambda x: x[-1]_
  File "<stdin>", line 1
    sorted(words, key = lambda x: x[-1]_
                                       ^
SyntaxError: invalid syntax
>>> 
>>> sorted(words, key = lambda x: x[-1])
['banana', 'apple', 'kiwi', 'mango']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> employees = [
...     {"name":"Alice", "salary":90000},
...     {"name":"Bob", "salary":75000},
...     {"name":"Charlie", "salary":90000},
...     {"name":"David", "salary":60000}
... ]
>>> 
>>> 
>>> 
>>> sorted_employees = sorted(employees, key = lambda x: (-x["salary"],x["name"])
... 
... 
... 
... 
... 
... print(s
  File "<stdin>", line 7
    print(s
    ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> s
{'name': 'Charlie', 'grade': 78}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> sorted_employees = sorted(employees, key = lambda x: (-x["salary"], x["name"]))
>>> print(sorted_employees)
[{'name': 'Alice', 'salary': 90000}, {'name': 'Charlie', 'salary': 90000}, {'name': 'Bob', 'salary': 75000}, {'name': 'David', 'salary': 60000}]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> """
... Lambda and sorting summary:
... 
... lambda x: x["field"] — sort by one field
... lambda x: (-x["num"], x["str"]) — sort by multiple, mix ascending/descending
... reverse=True — flips everything
... """
'\nLambda and sorting summary:\n\nlambda x: x["field"] — sort by one field\nlambda x: (-x["num"], x["str"]) — sort by multiple, mix ascending/descending\nreverse=True — flips everything\n'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> exit()

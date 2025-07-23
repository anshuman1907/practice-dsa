


Anshuman’s Python Coding Practice – 23 July 2025 (Text Format)

Level Up / Advanced Practice
----------------------------
1. Digit Frequency in Number
def digit_freq(n):
    freq = {}
    for digit in str(n):
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
    return freq
# Example: print(digit_freq(1122334411))
# Output: {'1': 4, '2': 2, '3': 2, '4': 2}

2. Capitalize First Letter of Each Word
text = "python is powerful and fun"
result = " ".join(word.capitalize() for word in text.split())
print(result)  # Output: Python Is Powerful And Fun

3. List of Dicts Filter: Names > 25 Age
users = [
    {"name": "Ansh", "age": 20},
    {"name": "Ravi", "age": 26},
    {"name": "Meena", "age": 30}
]
for u in users:
    if u["age"] > 25:
        print(u["name"])  # Output: Ravi, Meena

4. Sum of All Elements in a Nested List
nested = [[1, 2], [3, 4], [5, 6]]
s = 0
for sublist in nested:
    for val in sublist:
        s += val
print(s)  # Output: 21

5. Count Words Starting with a Vowel
def count_vowel_words(sentence):
    count = 0
    words = sentence.lower().split()
    for word in words:
        if word[0] in "aeiou":
            count += 1
    return count
# Example: print(count_vowel_words("I am an engineer and an artist"))  # Output: 4

Set, Nested Dict, Loop, and Short Notes
---------------------------------------
6. Nested Dictionary Access & Custom Extraction
students = {
    "s1": {"name": "Ansh", "age": 20, "city": "Patna"},
    "s2": {"name": "Meena", "age": 22, "city": "Delhi"},
    "s3": {"name": "Ravi", "age": 19, "city": "Bihar"}
}
# Access single value
print(students["s1"]["name"])  # Output: Ansh
# Custom: name from s1, age from s3, city from s2
name = ""
age = 0
city = ""
for key, val in students.items():
    if key == "s1":
        name = val["name"]
    if key == "s3":
        age = val["age"]
    if key == "s2":
        city = val["city"]
print("Name from s1:", name)
print("Age from s3:", age)
print("City from s2:", city)

7. Dictionary Loop with If-Else
marks = {"math": 75, "science": 42, "english": 90}
for subject, score in marks.items():
    if score >= 50:
        print(subject, "Pass")
    else:
        print(subject, "Fail")

Python Set Practice Quiz (Q1–Q5)
--------------------------------
Q1. Unique Elements Count
nums = [1, 2, 2, 3, 4, 4, 5, 1]
print(set(nums))           # {1, 2, 3, 4, 5}
print(len(set(nums)))      # 5

Q2. Common Elements (Intersection)
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b))   # {3, 4}

Q3. Add and Remove
s = set()
s.add(10)
s.add(20)
s.add(30)
s.remove(20)
print(s)                   # {10, 30}

Q4. Union
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))    # {1, 2, 3, 4, 5}

Q5. Is Subset?
s1 = {2, 3}
s2 = {1, 2, 3, 4}
if s1.issubset(s2):
    print("Yes")           # Yes
else:
    print("No")

Set Short Notes (Revision)
--------------------------
- set() se empty set banta hai, {} se dict.
- add(), update(), remove(), discard() methods use hote hain.
- Set me loop ka order random hota hai.
- .union(), .intersection(), .issubset(), .difference() are set operations.
- Interview me set ka use: unique values, fast lookup, math set ops.






#################
students = {
    "s1": {"name": "Ansh", "age": 20, "city": "Patna"},
    "s2": {"name": "Meena", "age": 22, "city": "Delhi"},
    "s3": {"name": "Ravi", "age": 19, "city": "Bihar"}
}

name = ""
age = 0
city = ""

for key, val in students.items():
    if key == "s2":
        name = val["name"]
    if key == "s3":
        age = val["age"]
    if key == "s2":
        city = val["city"]
        name = val["name"]

print(f"Name from s1: {name}")
print(f"Age from s3: {age}")
print(f"City from s2: {city}, and name is  {name}")




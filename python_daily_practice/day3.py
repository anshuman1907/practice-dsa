Anshuman’s Python Coding Practice – 24 July 2025

Q1. List: Find Second Largest Element
nums = [12, 44, 21, 9, 44, 31]
unique_nums = list(set(nums))
unique_nums.sort()
print(unique_nums[-2])
# Output: 31

Q2. Dict: Total of Even Values
marks = {"Ansh": 35, "Neha": 40, "Raj": 47, "Simran": 50}
s = 0
for key, val in marks.items():
    if val % 2 == 0:
        s += val
print(s)
# Output: 90

Q4. Tuple: Reverse All Elements
t = (11, 25, 7, 9, 30)
print(t[::-1])
# Output: (30, 9, 7, 25, 11)

Q5. String: Count Words
text = "learning python is fun and easy"
print(len(text.split()))
# Output: 6

Q10. Tuple: Print All Elements Except First and Last
t = (5, 8, 13, 21, 34, 55)
print(t[1:-1])
# Output: (8, 13, 21, 34)

---
File auto-generated for Anshuman by ChatGPT on 24 July 2025.

# Namaste JavaScript – Episode 19: map, filter & reduce

---

## 📌 Key Points

### 1. Map Function
- **Purpose**: Transforms each element in an array and returns a **new array**.
- **Syntax**: `const newArr = arr.map(callback);`

```javascript
const arr = [5, 1, 3, 2, 6];

// Double values
const doubleArr = arr.map(x => x * 2); // [10, 2, 6, 4, 12]

// Triple values
const tripleArr = arr.map(x => x * 3); // [15, 3, 9, 6, 18]

// Convert to binary strings
const binaryArr = arr.map(x => x.toString(2)); // ["101", "1", ...]
```

---

### 2. Filter Function
- **Purpose**: Creates a **new array** with elements that meet a condition.
- **Syntax**: `const filteredArr = arr.filter(predicateFn);`

```javascript
const arr = [5, 1, 3, 2, 6];

// Keep only odd numbers
const oddArr = arr.filter(x => x % 2); // [5, 1, 3]
```

---

### 3. Reduce Function
- **Purpose**: Reduces an array into a **single output** (value or object).
- **Syntax**: `const result = arr.reduce((acc, cur) => {/* logic */}, initialValue);`

```javascript
const arr = [5, 1, 3, 2, 6];

// Sum of elements
const sum = arr.reduce((acc, cur) => acc + cur, 0); // 17

// Find maximum
const max = arr.reduce((acc, cur) => (cur > acc ? cur : acc), 0); // 6
```

---

### 4. Tricky Map Example
Extract full names from user objects:
```javascript
const users = [
  { firstName: "Alok", lastName: "Raj", age: 23 },
  { firstName: "Ashish", lastName: "Kumar", age: 29 },
  { firstName: "Ankit", lastName: "Roy", age: 29 },
  { firstName: "Pranav", lastName: "Mukherjee", age: 50 },
];

const fullNames = users.map(user => user.firstName + " " + user.lastName);
// ["Alok Raj", "Ashish Kumar", ...]
```

---

### 5. Complex Reduce Example (Age Report)
Count users by age:
```javascript
const report = users.reduce((acc, curr) => {
  acc[curr.age] = (acc[curr.age] || 0) + 1;
  return acc;
}, {});
// { "23": 1, "29": 2, "50": 1 }
```

---

### 6. Function Chaining
Combine methods like `filter` and `map`:
```javascript
const result = users
  .filter(user => user.age < 30)
  .map(user => user.firstName);
// ["Alok", "Ashish", "Ankit"]

// Same logic using reduce:
const result2 = users.reduce((acc, curr) => {
  if (curr.age < 30) acc.push(curr.firstName);
  return acc;
}, []);
// ["Alok", "Ashish", "Ankit"]
```

---

## 📝 TL;DR Cheat Sheet

| Method       | Purpose                               | Returns             |
|--------------|----------------------------------------|---------------------|
| **map**      | Transform each array element           | New array           |
| **filter**   | Select elements based on condition     | New filtered array  |
| **reduce**   | Condense array to a single result      | Single value/object |
| **Chaining** | Combine methods for flow logic         | Clean, readable code|

---

# Namaste JavaScript – Episode 18: Higher-Order Functions ft. Functional Programming

---

## 📌 Key Points

### 1. What Is a Higher-Order Function (HOF)?
- A **higher-order function** is one that **accepts another function as an argument**, or **returns a function**, or does both.
```javascript
function sayHi() { console.log("Hi"); }
function outer(fn) { fn(); }
outer(sayHi); // 'sayHi' is passed as argument
```
- Here, `outer` is the HOF, and `sayHi` is the callback.

---

### 2. Why Use Functional Programming?
- Follows **DRY (Don't Repeat Yourself)** principle.  
- HOFs prevent rewriting similar logic multiple times.  

---

### 3. Example: Calculating Circle Properties
Instead of separate loops for area, circumference, and diameter:
```javascript
calculate(circles, areaFn);
calculate(circles, circumferenceFn);
```
- `calculate` is the reusable **HOF**, specific operations (area, circumference) are passed as callbacks.

---

### 4. Implementing Map via HOF
Custom polyfill for `Array.prototype.map`:
```javascript
Array.prototype.myMap = function(fn) {
  const result = [];
  for (let item of this) {
    result.push(fn(item));
  }
  return result;
};
```
- Demonstrates how HOFs enable array transformations.

---

### 5. Key Takeaways
- **DRY principle** → reduce repetition.  
- Use functions to abstract repeated patterns.  
- **Higher-order functions** accept or return functions.  
- Works because JS treats functions as **first-class citizens**.  

---

## 📝 TL;DR Cheat Sheet

| Concept                 | Insight |
|-------------------------|---------|
| Higher-Order Function   | Accepts or returns functions; key to functional patterns |
| DRY Principle           | Reduce repetition via HOFs |
| Callback Flexibility    | Pass different behavior into HOF via callbacks |
| Map Polyfill            | Example of HOF in action on array transformations |
| First-Class Functions   | Core JS feature enabling this pattern |

---

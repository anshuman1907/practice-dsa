# Namaste JavaScript – Episode 10: Closures in JS

Closures are one of the most fundamental concepts in JavaScript and a frequent interview favorite.

---

## 📌 Key Points

### Closure Definition
A function bundled together with its lexical scope is called a **closure**.  
It allows the function to remember its outer variables even after the outer function has executed.

---

### How It Works
**Example 1:**
```javascript
function x() {
  var a = 7;
  function y() {
    console.log(a);
  }
  return y;
}
var z = x();
z(); // logs 7
```
- Even when `x()` finishes, `z()` continues to have access to `a`.

**Example 2 (Nested Closures):**
```javascript
function z() {
  var b = 900;
  function x() {
    var a = 7;
    function y() {
      console.log(a, b);
    }
    y();
  }
  x();
}
z(); // logs 7, 900
```
- Inner functions retain access to all variables in their outer chain.

---

### Simple Explanation
A closure is a function that retains access to variables from its outer (lexical) function, even after that function has returned.

---

### Advantages of Closures
- **Module Design Pattern** – enables data privacy and encapsulation.  
- **Currying** – creating functions with preset arguments.  
- **Memoization** – caching results for efficiency.  
- **Data Hiding & Encapsulation** – hide implementation details.  
- **Async/Timers** – used with `setTimeout()` and callbacks.

---

### Drawbacks of Closures
- Extra memory consumption.  
- Possible memory leaks if closures retain large objects longer than needed.  
- May cause browser slowdowns/freezing if misused.

---

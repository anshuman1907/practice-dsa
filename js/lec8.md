# Namaste JavaScript – Episode 11: setTimeout + Closures (Interview Question)

---

## 📌 Key Points

### 1. setTimeout & Execution Order
```javascript
function x() {
  var i = 1;
  setTimeout(function () {
    console.log(i);
  }, 3000);
  console.log("Namaste Javascript");
}
x();
```
- Output:
  - `Namaste Javascript` (runs immediately – synchronous)
  - After 3 seconds → `1`
- `setTimeout` callback forms a closure over `i`.

---

### 2. Loop + setTimeout with `var`
```javascript
function x() {
  for (var i = 1; i <= 5; i++) {
    setTimeout(function () {
      console.log(i);
    }, i * 1000);
  }
  console.log("Namaste Javascript");
}
x();
```
- Output:
  - `Namaste Javascript`
  - After delays: `6 6 6 6 6`
- Reason: All callbacks share the same `i` (closure captures reference, not value).

---

### 3. Fix Using `let`
```javascript
for (let i = 1; i <= 5; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 1000);
}
```
- Output: `1 2 3 4 5` (each logged after respective seconds).
- `let` creates new block-scoped `i` for each iteration.

---

### 4. Fix Using `var` + Closure Function
```javascript
for (var i = 1; i <= 5; i++) {
  (function close(i) {
    setTimeout(function () {
      console.log(i);
    }, i * 1000);
  })(i);
}
```
- Here each iteration passes its own `i` to an IIFE, creating a new closure.

---

### 5. Why Important for Interviews
- Tests knowledge of:
  - Event loop & async execution
  - Difference between `var` and `let`
  - How closures capture variables
- Classic JS interview puzzle.

---

## ✅ Summary
- `setTimeout` + `var` in loops → prints last value.  
- Fixes:
  - Use `let` (block scope).  
  - Or use IIFE/extra function with `var`.  
- Demonstrates closures + async behavior.

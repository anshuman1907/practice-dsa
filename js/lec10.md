# Namaste JavaScript – Episode 14: Callback Functions in JS ft. Event Listeners

---

## 📌 Key Points

### 1. Callback Functions
- Functions are *first-class citizens*—they can be passed as arguments.  
- When you pass function **A** into function **B**, **A** becomes a *callback*.  
```javascript
setTimeout(function () {
  console.log("Timer");
}, 1000);
```

---

### 2. Sync Language, Async Power
- JS is synchronous and single-threaded.  
- Callbacks enable asynchronous tasks.  
```javascript
function x(y) {
  console.log("x");
  y();
}
x(function y() {
  console.log("y");
});
```
- Output: `x → y → (after timeout) timer`.

---

### 3. Main Thread Blocking Warning
- JS engine has a **single call stack**.  
- Long-running functions block the stack (e.g., 30s loop).  
- This is called **blocking the main thread** → avoid it.

---

### 4. Nested Callbacks (Callback Hell)
```javascript
printStr("A", () => {
  printStr("B", () => {
    printStr("C", () => {});
  });
});
```
- Hard to read & maintain → **Callback Hell / Pyramid of Doom**.

---

### 5. Event Listeners
**Basic Example:**
```html
<button id="clickMe">Click Me!</button>
```
```javascript
document.getElementById("clickMe").addEventListener("click", function xyz() {
  console.log("Button clicked");
});
```

**With Closure (Better):**
```javascript
function attachEventList() {
  let count = 0;
  document.getElementById("clickMe").addEventListener("click", function xyz() {
    console.log("Button clicked", ++count);
  });
}
attachEventList();
```
- Keeps `count` private inside closure.

---

### 6. Memory & Garbage Collection Caveat
- Event listeners create closures → can retain variables in memory.  
- Always **remove event listeners** when no longer needed to free memory.

---

## 📝 TL;DR Cheat Sheet

| Concept                    | Insight |
|----------------------------|---------|
| Callback Functions         | Pass function into another for async tasks |
| Sync Core, Async via Callbacks | Single-threaded JS + Web APIs enable async |
| Blocking Warning           | Long sync code blocks the call stack |
| Callback Hell              | Deep nesting makes code unreadable |
| Event Listeners            | Attach callbacks to DOM events |
| Memory Cleanup             | Remove unused listeners to avoid leaks |

---

# Namaste JavaScript – Episode 15: Asynchronous JavaScript & Event Loop from Scratch

---

## 📌 Key Points

### 1. JavaScript Is Synchronous & Single-Threaded
- JS handles one operation at a time, executing in a single call stack.
- No built-in waiting or delay—executes instructions sequentially.

---

### 2. Call Stack & Execution Context
- JS runtime starts with **Global Execution Context (GEC)** pushed to the call stack.
- Each function call creates and pushes a new Execution Context onto the stack.

---

### 3. Web APIs — Not Part of JS Engine
- Features like `setTimeout`, `fetch`, DOM methods, `console.log`, `localStorage` are provided by the **browser environment (Web APIs)**, not the JS engine itself.
- Accessed via the global `window` object.

---

### 4. setTimeout & Callback Queue Workflow
```javascript
console.log("start");
setTimeout(function cb() {
  console.log("timer");
}, 5000);
console.log("end");
```
- Flow:
  - "start" → logs immediately
  - "end" → logs immediately
  - `cb()` scheduled in Web API timer
  - After 5s → moved to **Callback Queue**
  - **Event Loop** shifts `cb()` into stack once it's empty

---

### 5. Interactive Example with Event Listener
```javascript
console.log("Start");
document.getElementById('btn').addEventListener('click', function cb() {
  console.log("Callback");
});
console.log("End");
```
- Callback registered in Web APIs environment
- On user click → callback enters **Callback Queue**
- Event Loop moves it to call stack when free

---

### 6. Event Loop as Gatekeeper
- Constantly checks:
  - Is the call stack empty?
  - Any callbacks in the queue?
- If yes → pushes queued callbacks to the stack.

---

### 7. Microtask Queue (Promises) vs Callback Queue
- Promise `.then()` callbacks → go to **Microtask Queue**
- Event Loop always processes Microtasks **before** Callback Queue
- Ensures promises get higher priority.

---

## 📝 TL;DR Cheat Sheet

| Concept                     | Insight |
|-----------------------------|---------|
| JS Execution                | Synchronous & single-threaded |
| Call Stack & Execution Context | Manages function invocations |
| Web APIs                    | Provided by browser, not engine |
| Callback Queue              | Stores async tasks awaiting execution |
| Event Loop                  | Moves tasks from queue → stack |
| Microtask Queue             | Promise callbacks, higher priority |

---

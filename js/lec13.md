# Namaste JavaScript – Episode 17: Trust Issues with setTimeout()

---

## 📌 Key Points

### 1. `setTimeout()` Isn’t Exact
- `setTimeout()` schedules a callback, but doesn’t guarantee it runs *exactly* after the specified delay.
- If the **call stack** is busy (e.g., during heavy synchronous computation), the callback waits in the **callback queue** until the stack is clear—even if the delay has elapsed.

---

### 2. Example Scenario
```javascript
setTimeout(() => console.log("Hi"), 0);
while (true) {
  // long-running loop
}
```
- Despite using a `0ms` delay, the `"Hi"` log may not appear until after the loop finishes because the stack remains occupied.  
- Delays are minimum waits, not guarantees.

---

### 3. Why This Happens
- JS is **single-threaded**: only one task executes at a time.
- The **Event Loop** moves callbacks into execution only once the stack is clear.
- Heavy blocking code delays callbacks—even those with `0ms` timeout.

---

### 4. Takeaway for Devs
- Track down and avoid main-thread blocking.
- Don’t assume `setTimeout(fn, 0)` is instant—it’s deferred until the stack is free.
- Use asynchronous patterns (Promises, async/await, offloading heavy logic) to keep the thread responsive.

---

## 📝 TL;DR Cheat Sheet

| Concept                   | Insight |
|---------------------------|---------|
| `setTimeout()` Timing     | Schedules callback, but execution depends on call stack availability |
| `0ms` Delay ≠ Instant     | Even `0ms` timers get delayed if stack is busy |
| JS Concurrency Model      | Single-threaded; Event Loop only pushes queued callbacks when stack is clear |
| Best Practice             | Avoid blocking code; prefer async strategies for smooth execution |

---

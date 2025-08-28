# Notes: `let` and `const` in JavaScript — Temporal Dead Zone (TDZ)

## Hoisting Behavior
- `let` and `const` **are hoisted**, but they aren’t initialized immediately.
- They reside in a memory area separate from `var` (often called *script scope*), not accessible before initialization.

## Temporal Dead Zone (TDZ)
- **TDZ** is the period from the start of a block until the variable is declared and initialized.
- Trying to access a `let` or `const` variable before its declaration triggers a **ReferenceError**.

## Memory Allocation & Access
- In the debugger’s memory view, `let`/`const` appear as `undefined` before initialization—but stored in a separate “script” area, not the global `window`.
- Unlike `var`, `let`/`const` do **not** become properties of the `window` object.

## Error Types: `SyntaxError`, `ReferenceError`, and `TypeError`
1. **ReferenceError** — Accessing `let`/`const` within their TDZ.
2. **SyntaxError** — Occurs when syntax rules are violated (e.g. missing initializer for `const`).
3. **TypeError** — Happens when trying to reassign a constant variable (`const`).

## Declarations & Re-declarations
- You **cannot redeclare** a variable declared with `let` or `const`.
- `const` must be initialized **at declaration**—you cannot declare it without an initial value.
- `var` is more permissive: can be re-declared, hoisted in the global scope, and no TDZ applies.

## Best Practices Summary
- Prefer `const` by default; use `let` only when variable reassignment is necessary.
- Avoid `var` unless needed for legacy compatibility.
- Declare and initialize `let`/`const` at the **top of their block** to minimize TDZ.

---

## TL;DR Comparison

| Keyword | Hoisted? | Accessible before init? | Scope           | Re-declarable? | Re-assignable? |
|---------|----------|--------------------------|----------------|----------------|----------------|
| `var`   | Yes      | Yes (as `undefined`)     | Function/global | Yes            | Yes            |
| `let`   | Yes      | **No** (ReferenceError)  | Block scope     | No             | Yes            |
| `const` | Yes      | **No** (ReferenceError)  | Block scope     | No             | **No**         |

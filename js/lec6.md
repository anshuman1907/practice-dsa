# Block Scope & Shadowing in JavaScript

*Namaste JavaScript -- Episode 9*

------------------------------------------------------------------------

## 1. What is a Block?

-   A block is any chunk of code enclosed within `{ … }`.\
-   Examples: `if`, `for`, `while` loops, or standalone grouped
    statements.\
-   Blocks help create **scopes**.

------------------------------------------------------------------------

## 2. Block Scope

-   Variables declared with **`let`** and **`const`** are confined to
    the block they're defined in.\
-   Unlike `var`, they don't leak outside the block.\z
-   Safer and cleaner scoping.

------------------------------------------------------------------------

## 3. Shadowing

-   Happens when a variable in the inner (nested) scope has the **same
    name** as one in the outer scope.\
-   Inner variable shadows the outer one in its scope.

``` js
const x = 10;
{
  const x = 20;
  console.log(x); // 20 — inner x shadows outer x
}
console.log(x); // 10 — outer x still intact
```

------------------------------------------------------------------------

## 4. Illegal Shadowing

-   Some combinations aren't allowed:
    -   Example: declaring `var` in the inner scope while `let/const`
        exists in the outer scope.\
-   JavaScript enforces scoping boundaries to prevent this.

------------------------------------------------------------------------

## 5. Underlying Mechanics

-   **Lexical Scoping**:
    -   Inner scopes search upwards in the scope chain to resolve
        variables.\
    -   If not found → continue to parent scopes → finally global → if
        still missing → **ReferenceError**.

------------------------------------------------------------------------

## TL;DR

-   **Block** = `{}`\
-   **`let`/`const`** = block-bound\
-   **Shadowing** = inner variable hides outer variable\
-   **Illegal Shadowing** = `var` cannot shadow `let/const`\
-   **Scope chain** = search inside → parent → global → error

------------------------------------------------------------------------

## 📌 Block Scope & Shadowing Summary

| Concept            | `var`                                  | `let` / `const`                       |
|--------------------|-----------------------------------------|----------------------------------------|
| **Scope Type**     | Function / Global scope                | Block scope (`{ }`)                    |
| **Hoisting**       | Hoisted, initialized as `undefined`    | Hoisted but in TDZ (Temporal Dead Zone)|
| **Block Access**   | Accessible outside block               | Not accessible outside block           |
| **Shadowing Rules**| `var` can shadow `var` (allowed)       | `let` can shadow `let` (allowed)       |
| **Cross Shadowing**| `var` → can be shadowed by `let` ✅     | `let` → cannot be shadowed by `var` ❌ |
| **Lexical Scope**  | Still follows lexical environment      | Each block has its own lexical scope   |
| **Arrow Functions**| Same scope rules as normal functions   | Same scope rules as normal functions   |

---

⚡ **TL;DR**: Use `let`/`const` for predictable block scoping, avoid `var` unless you like debugging at 3 AM.  
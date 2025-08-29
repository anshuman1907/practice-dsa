# Namaste JavaScript – Episode 13: First-Class Functions & Anonymous Functions

---

## 📌 Key Points

### Function Statement (Declaration)
A named function, fully **hoisted**. You can call it even before it’s defined:
```javascript
function a() {
  console.log('Hello');
}
a(); // Hello
```

---

### Function Expression
Assigned to a variable, not hoisted like declarations:
```javascript
var b = function() {
  console.log('Hello');
};
b();
```

---

### Statement vs Expression (Hoisting Difference)
- Declarations are hoisted—callable before they appear.
- Expressions behave like variables: until assigned, they're `undefined`.

```javascript
a(); // Works
b(); // TypeError – b is undefined

function a() { console.log('Hello A'); }
var b = function() { console.log('Hello B'); };
```

---

### Anonymous Function
A function without a name. Invalid alone—a syntax error. Must be used in expressions:
```javascript
function() { } // SyntaxError
```

---

### Named Function Expression
Like an expression but with a name—helps in recursion and debugging. Name is scoped locally:
```javascript
var b = function xyz() {
  console.log('b called');
};
b();      // Works
xyz();    // ReferenceError – not in outer scope
```

---

### Parameters vs Arguments
- **Parameters**: placeholders in function definitions.  
- **Arguments**: actual values passed during invocation.

```javascript
var b = function(param1, param2) { … };
b(arg1, arg2);
```

---

### First-Class Functions (First-Class Citizens)
Functions in JS are **values**:
- Can be **assigned** to variables.  
- **Passed** as arguments.  
- **Returned** from other functions.  

```javascript
b(function () {});        // passing
console.log(b());         // returning a function
```

---

## 📝 TL;DR Cheat-Sheet

| Concept                  | Summary |
|--------------------------|---------|
| Function Declaration     | Named, hoisted, call-anytime |
| Function Expression      | Not hoisted, used as value |
| Anonymous Function       | Name-less, must be in expression |
| Named Function Expr      | Scoped name, for recursion/debugging |
| Parameters vs Arguments  | Declarations vs passed values |
| First-Class Functions    | Functions as variables, arguments, returns |

---

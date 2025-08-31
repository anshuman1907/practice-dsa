

function Person(name, age, city) {
  this.name = name;
  this.age = age;
  this.city= city

  this.city;
}
const p1 = new Person("Ashu", 28,"bbk");
// console.log(p1.name,p1.age,p1.city); 




// Destructuring

// Extract values from arrays/objects.
const [a, b] = [1, 2];
const {name, age} = {name: "Ashu", age: 28};


console.log(a,b,name,age)


const arr = [1, 2, 3];
// console.log([...arr, 4, 5]); // [1,2,3,4,5]
console.log([...arr, 4,6,7,5]); // [1,2,3,4,5]

async function getUserData() {
  try {

    let response = await fetch("https://jsonplaceholder.typicode.com/users/1");

   
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    var data = await response.json();
    console.log("User Data:", data);

  } catch (error) {

    console.log("Failed to fetch user data:", error.message);
  } finally {
    console.log("Request completed ");
  }
}

// getUserData();



function Person(name, age, city) {
  this.name = name;
  this.age = age;
  this.city= city

  this.city;
}
const p1 = new Person("Ashu", 28,"bbk");
console.log(p1.name,p1.age,p1.city); 

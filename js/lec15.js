// map filter redusce 

// map

const arr = [1, 2, 4, 5, 3]

function double(x) {
    return x * 2
}
const output = arr.map(double)

console.log(output)



function triple(x) {
    return x * 3
}
const output1 = arr.map(triple)


console.log(output1)


// in Binary

function binary(x) {
    return x.toString(2)

}
const output2 = arr.map(binary)

console.log(output2)


// 2nd methode


const output3 = arr.map((x) => x.toString(2))

console.log(output3)





// Filter function 

const arr1 = [1, 3, 5, 6, 8, 2]

function isodd(x) {
    return x % 2
}
const out = arr1.filter(isodd)

// //////

function iseven(x) {
    return x % 2 == 0
}


const out1 = arr1.filter(iseven)
console.log(out1)


// in arrow dfunction waay 

const out4 = arr1.filter((x) => x > 4)

console.log(out4)


// reduce fucntion 


const arr2 = [1, 2, 63, 4, 7]



const out5 = arr2.reduce(function (sum, curr) {
    sum = sum + curr;
    return sum;

}, 0)

console.log(out5)

// max in  arr2

const out6 = arr2.reduce(function (max, curr) {
    if (curr > max) {
        max = curr
    }
    return max
}, 0)

console.log(out6)


// using aroow function 
 
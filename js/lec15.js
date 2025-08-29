// map filter redusce 

// map

const arr=[1,2,4,5,3]

function double(x){
    return x*2
}
const output=arr.map(double)

console.log(output)



function triple(x){
    return x*3
}
const output1=arr.map(triple)


console.log(output1)


// in Binary

function  binary(x){
    return x.toString(2)

}
const output2=arr.map(binary)

console.log(output2)


// 2nd methode


const output3=arr.map((x) => x.toString(2))

console.log(output3)

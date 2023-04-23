let countries = ['Vietnam', 'China', 'USA', 'Japan', 'Brazil', 'Mexico', 'Canada']

// assign and indexing, array is mutable
countries[0] = 'Vietnam is GREAT'
console.log(countries)

// string is immutable
let myName = 'Kasim'
myName[0] = 'Q'
console.log(myName[0])

// number of items in array
console.log(countries.length)

// array
var myArr = ['one', 'two', 'three']

// python .append
myArr.push('four')
console.log(myArr)

// same as python list pop
myArr.pop()
console.log(myArr)

//array last index
console.log(myArr[myArr.length - 1])

//array iteration
var arr = ['A', 'B', 'C', 'D', 'E']
for(var i = 0; i < arr.length; i++) {
    console.log(arr[i])
}

// more like python for loop
for (letter of arr){
    console.log(letter);
}

// forEach iteration + func
function addAwesome(name){
    console.log(name + ' is awesome!')
}

let namesArr = ['Kasim', 'Hashim', 'Ali', 'Sara']

namesArr.forEach(addAwesome)
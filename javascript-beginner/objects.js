// key does not need to be inst as string
var carInfo = {make:'Toyota', model:'Corolla', year:2020};

// key is inside ' '
console.log(carInfo['make']);
console.log(carInfo['model']);
console.log(carInfo['year']);

var myNewO = {a:'Hello', b:[1, 2, 3, 4], c:{inside:['a', 'b', 'c']}};

// accessing an object
console.log(myNewO.a);
console.log(myNewO.b[1]);
console.log(myNewO.c['inside'][1]);

// changing values
carInfo.year = 2021;

// has been updated
console.log(carInfo);


// changing values as reference
carInfo.year -= 1;

// has been updated
console.log(carInfo);

// looping through objects
for (key in carInfo) {
    // print keys
    console.log(key);
    // print key values
    console.log(carInfo[key]);
}

var pokemonInfo = {
    name: 'Bulbasaur',
    type: 'grass',
    hp: 45,
    attack: 49,
    defense: 49,
    speed: 45,
    pokemonAlert: function(){
        // this acts as a reference to the object
        return this.name
    }
};

// logs bulbasaur
console.log(pokemonInfo.pokemonAlert());

// simple object with function
var myObj = {
    name: 'Jake',
    greet: function(){
        console.log(this.name);
    }
};

// logs Jake
myObj.greet();


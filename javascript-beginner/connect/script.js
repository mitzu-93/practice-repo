var x = 1;

while (x <= 20) {
    if (x % 3 === 0 && x % 5 === 0) {
        console.log("FizzBuzz");
        console.log(x);
    } else if (x % 3 === 0) {
        console.log("Fizz");
        console.log(x);
    } else if (x % 5 === 0) {
        console.log("Buzz");
        console.log(x);
    }
    x++;
}
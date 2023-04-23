function start() {

    // inside a function, we can use let or var     
    for (let x = 0; x < 10; x++)
        console.log(x);

    // outside a function, we can't use let but we can use var
    console.log(x);
    }

start()
var base = 10
var increment = 5

function poison(base, increment){
    let total_damage = base + increment
    return total_damage * Math.random()
}

// prints since var is global and assigned to window.x
let psn_dmg = poison(base, increment)
console.log(psn_dmg)

// following is not global and thus error
console.log(total_damage)


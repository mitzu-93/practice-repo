var hot = false
var temp = 30

if (temp>80) {
    hot = true
    console.log(hot)
    console.log("Temp is greater than 80")
}else if (temp<=80 && temp>=50){
    console.log("Temp is okay!")
}else {
    console.log("Temp is below 50")
}
const display = document.querySelector("input")
const buttons = document.querySelectorAll("button")

console.log(display.value);


buttons.forEach(e => {
    e.addEventListener('click', () => {
        if (e.innerText == "C") {
            display.value = "0"
        } else if (e.innerText == "+") {
            display.value += e.innerText
        } else if (e.innerText == "-") {
            display.value += e.innerText
        } else if (e.innerText == "*") {
            display.value += e.innerText
        } else if (e.innerText == "/") {
            display.value += e.innerText
        } else if (e.innerText == "=") {
            display.value = eval(display.value)
        } else {
            display.value += e.innerText
        }

        if(display.value== "0"){
            display.value =""
        }
    })

})


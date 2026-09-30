const num1 = document.querySelector("#num1");
const num2 = document.querySelector("#num2");
const result = document.querySelector("#result");

function calculate(operation) {
    const a = Number(num1.value);
    const b = Number(num2.value);
    let answer;

    if (operation === "add") {
        answer = a + b;
    } else if (operation === "subtract") {
        answer = a - b;
    } else if (operation === "multiply") {
        answer = a * b;
    } else if (operation === "divide") {
        if (b === 0) {
            result.textContent = "Result: Cannot divide by zero";
            return;
        }
        answer = a / b;
    }

    result.textContent = "Result: " + answer;
}

document.querySelector("#add").addEventListener("click", () => {
    calculate("add");
});

document.querySelector("#subtract").addEventListener("click", () => {
    calculate("subtract");
});

document.querySelector("#multiply").addEventListener("click", () => {
    calculate("multiply");
});

document.querySelector("#divide").addEventListener("click", () => {
    calculate("divide");
});
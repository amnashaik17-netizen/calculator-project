let exp = document.getElementById("expression");
let res = document.getElementById("result");
let historyList = document.getElementById("historyList");

let current = "";

/* Append */
function append(val) {
    current += val;
    exp.innerText = current;

    try {
        res.innerText = eval(current);
    } catch {
        res.innerText = "";
    }
}

/* Calculate */
function calculate() {
    try {
        let answer = eval(current);
        addToHistory(current + " = " + answer);

        current = answer.toString();
        res.innerText = current;
        exp.innerText = "";
    } catch {
        res.innerText = "Error";
    }
}

/* History */
function addToHistory(item) {
    let li = document.createElement("li");
    li.innerText = item;
    historyList.appendChild(li);
}

/* Clear */
function clearAll() {
    current = "";
    exp.innerText = "";
    res.innerText = "0";
}

/* Backspace */
function backspace() {
    current = current.slice(0, -1);
    exp.innerText = current;
}

/* Square root */
function sqrt() {
    try {
        current = Math.sqrt(eval(current)).toString();
        res.innerText = current;
    } catch {
        res.innerText = "Error";
    }
}

/* Theme toggle */
function toggleTheme() {
    document.body.classList.toggle("light");
}

/* Keyboard */
document.addEventListener("keydown", e => {
    if (!isNaN(e.key) || "+-*/.".includes(e.key)) append(e.key);
    if (e.key === "Enter") calculate();
    if (e.key === "Backspace") backspace();
});
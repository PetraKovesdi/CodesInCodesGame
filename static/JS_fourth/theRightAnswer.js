console.log("Hello, this is a console message.");
let btn = document.querySelector("button.first");
let btn2 = document.querySelector("button.second");
let submissionField = document.querySelector("div.solution-submission");
let btnRightAnswerQuery = document.querySelector("#solution-query");

function colors() {
    btn.style.backgroundColor = "lightgreen";
    };

    btn.onclick = colors;
    btn.addEventListener("click", function(){btn2.style.display = "inline"});
    btn.addEventListener("click", function(){btn.innerHTML = "Yes, you are curious."});

function colors2() {
     btn.style.backgroundColor = "aqua"
    };

    btn2.onclick = colors2;


let solution = function() {
    let Number = parseInt(document.querySelector("input#number").value);
    if (isNaN(Number)) {alert("A number is needed here.")}
    else if (Number == 664474) {alert("Yes"); submissionField.className = "colored-background solution-submission"}
    else {alert("No")}
    };

    btnRightAnswerQuery.onclick = solution;


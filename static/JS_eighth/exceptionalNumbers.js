console.log("Hello from exceptionalNumbers.");


function findThoseExceptNum (firstNum, secondNum) {
    try {
        if ( ( ! isNaN(firstNum)) && ( ! isNaN(secondNum))) {
            console.log("Value1: ", Math.random() * 100000 / (8168 % firstNum));
            console.log("Value2: ", Math.random() * 100000 / (10201 % secondNum));
        }else {
            console.log("2 numbers needed for input.");
        }

    } catch (error) {
        console.log(error)
    }
}


function isThisTheSolution (firstNum, secondNum) {
    let possibleSolution = firstNum * secondNum;
    let message = "";
    if (possibleSolution >= 100000 && possibleSolution < 1000000){
        message = "maybe yes";
    } else {
        message = "surely not";
    }
    console.log(`Is ${possibleSolution} the solution? `, message)
}

let checkSolution = function (first, second) {
    findThoseExceptNum(first, second);
    isThisTheSolution(first, second);
}

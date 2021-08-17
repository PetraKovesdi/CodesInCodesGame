console.log("Hello, this is a console message.");


let calcSolution = function () {
    let sum = 0;
    let numbers = [11954, 45170, 20396, 12082, 70127, 32731];
    for (i=0; i< numbers.length; i++) {sum = sum + numbers[i] + (missingNumber * i)};
    console.log(sum);
};
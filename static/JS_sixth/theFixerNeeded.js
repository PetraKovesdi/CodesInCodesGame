console.log("Hello, this is a console message.");

let firstSum, secondSum, thirdSum;
let numbers1, numbers2, numbers3;

firstSum = 0;
numbers1 = ["17935732, 32816809, 97625987, 51128149, 92158455"];
function calcFirstSum () {firstSum = 0; for ( let i = 0; i < numbers1.length; i++) { firstSum += numbers1[i]}; console.log(firstSum)};

secondSum= 0;
numbers2 = [79357621, 1120, 2791, 5366, 4489];
function calcSecondSum () {secondSum = 0; for (let i = 1; i < numbers2.length; i++) { secondSum += numbers2[i]}; console.log(secondSum)};

thirdSum = 0;
numbers3 = [54, 71, 19, 29, 81];
function calcThirdSum () {thirdSum= 0; for (let i = 0; i < numbers3.lengh; i++) { thirdSum += numbers3[i]}; console.log(thirdSum)};

calcFirstSum();
calcSecondSum();
calcThirdSum();

function calcSolution () {let solution = parseInt((firstSum - secondSum) / thirdSum);
     console.log((solution))};



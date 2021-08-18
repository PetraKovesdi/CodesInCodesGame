console.log("Hello, this is a console message.");

const INITIAL_NUM = 407331;


let functionsForCombination = {

    "80":
        function (number) {
            let newNum = number + 115;
            if (newNum >= 1000000) {
                newNum = newNum - 923;
            }
            return newNum;
        },

    "35":
        function (number) {
            let newNum = number - 308;
            if (newNum < 100000) {
                newNum = newNum + 638;
            }
            return newNum;
        },

    "57":
        function (number) {
            let newNum = number * 2;
            if (newNum >= 1000000) {
                let numStr = String(newNum);
                newNum = parseInt(numStr.substring(0,numStr.length-1));
            }
            return newNum;
        },

    "41":
        function (number) {
            let strNumArray = String(number).split("");
            let reverseArray = strNumArray.reverse();
            reverseArray[0] = reverseArray[0] == "0" ? "1" : reverseArray[0];
            let reverseStr = reverseArray.join("");
            let reverseNum = parseInt(reverseStr);
            return reverseNum;
        },

    "85":
        function (number) {
            let strNumArray = String(number).split("");
            let rotationKey = 3;
            let rotatedArray = [];
            for (let index = 0; index < strNumArray.length; index++){
                let newIndex = (index + rotationKey) % 6;
                rotatedArray.push(strNumArray[newIndex]);
            }
            rotatedArray[0] = rotatedArray[0] == "0" ? "3" : rotatedArray[0];
            let rotatedStr = rotatedArray.join("");
            let rotatedNum = parseInt(rotatedStr);
            return rotatedNum;
        },

    "72":
        function (number) {
            let strNumArray = String(number).split("");
            let swapsArray = strNumArray;
            for (let i = 0; i < ((strNumArray.length / 2) | 0) * 2; i += 2) {
                let temp = swapsArray[i];
                swapsArray[i] = swapsArray[i+1];
                swapsArray[i+1] = temp;
            }
            swapsArray[0] = swapsArray[0] == "0" ? "2" : swapsArray[0];
            let swapsStr = swapsArray.join("");
            let newNum = parseInt(swapsStr);
            return newNum;
        }

}


function calcCombinationForSolution(...keyNumbers){
    let newNum = INITIAL_NUM;

    try {
        for (keyNumber of keyNumbers) {
            if ( ! Object.keys(functionsForCombination).includes(String(keyNumber))){
                console.log(`${keyNumber} is not a valid input for this function to work properly.`);
                return;
            }
            newNum = functionsForCombination[String(keyNumber)](newNum);
        }
    } catch (error) {
        console.log(error);
        console.log("2-digit numbers needed for the argument.")
        return;
    }

    console.log(newNum);
}

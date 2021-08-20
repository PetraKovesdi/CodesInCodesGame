
function messageFromDecryptionModule (){
    console.log("Hello from module for decryption.")
}


function decryptRailFence(message, key=5){
    let decryptArray = [];
    // These will be the indices for the substrings in the decryptArray,
    // this will also show the starting index for each substring
    let listIndex = 0;
    let index = 0;
    let upwardIndex = 0;
    // For each substring setting starting length,
    // for key 5 there will be 5 substrings if length of message is 5 or longer
    let substringLength = 1;
    let messageCopy = message;
    while (listIndex < key){
        index = listIndex; //listIndex will be increased by one at end of each cycle
        substringLength = 1;
        while (index < message.length){

            if (listIndex > 0 && listIndex < key-1){
                //Not top or bottom points
                upwardIndex = index;
                upwardIndex = upwardIndex + (key * 2 - 2) - listIndex * 2;
                if (upwardIndex < message.length) {
                    substringLength++;
                }
            }

            index += key * 2 - 2; //Distance of points in same row in every downwards diagonal line
            if (index < message.length) {
                substringLength++;
            } else {
                break;
            }
        }
        decryptArray.push(messageCopy.substring(0,substringLength));
        messageCopy = messageCopy.substring(substringLength);
        listIndex++;
    }

    let decryptedMessage = "";

    //Downward and upward rebuilding of orig message
    while (decryptedMessage.length < message.length) {

        //Downward
        for (let i = 0; i < decryptArray.length; i++) {
            if (0 < decryptArray[i].length) {
                let letter = decryptArray[i].charAt(0);
                decryptArray[i] = decryptArray[i].substring(1);
                decryptedMessage += letter;
            }
        }

        //Upward
        for (let j = decryptArray.length-2; j > 0; j--) {
            if (0 < decryptArray[j].length) {
                let letter = decryptArray[j].charAt(0);
                decryptArray[j] = decryptArray[j].substring(1);
                decryptedMessage += letter;
            }
        }

    }
    return decryptedMessage;
}

export {messageFromDecryptionModule, decryptRailFence};
import { messageFromDecryptionModule, decryptRailFence } from './decryptRailFence.js';

console.log("Hello, this is a console message.");
console.log(messageFromDecryptionModule());


let showBtn = document.querySelector("#get-data");
let displayParagraph = document.querySelector("#content-field p");


showBtn.onclick = function() {
    showHiddenElements();
    getContent();
    }


function showHiddenElements(){
    let hiddenFields = document.querySelectorAll(".hidden");
    if (hiddenFields.length > 0) {
        for (let element of hiddenFields) {
            element.style.visibility = "visible";
            element.style.opacity = "1";
        }
    }
}

function getContent(){
    fetch("/eighth/api")
        .then(res => res.json())
        .then((data) => {console.log(data);
                        return Promise.resolve(data)})
        .then((data) => {
            new Promise((resolve,reject) =>
            { if (Object.keys(data).includes("message") && data.message !== "") {
                displayContent(data.message);
                resolve(data);
            } else {
                reject("No message received.")
            }
            })})
        .then(()=> {
            addListenerToDecriptBtn();
            showBtn.onclick = ()=>{};
        })
        .catch(error => console.log(error))
}

function displayContent(message){
    displayParagraph.innerText = message;
    displayParagraph.dataset.message = message;
}

function addListenerToDecriptBtn(){
    let decryptBtn = document.querySelector("#decrypt-data");
    decryptBtn.onclick = function () {
        console.log("Hello decryption module");
        let message = document.querySelector("div#content-field p").dataset.message;
        hideElement(displayParagraph);
        let decryptedMessage = decryptRailFence(message);
        displayContent(decryptedMessage);
        showHiddenElements();
        console.log(decryptedMessage);

        decryptBtn.onclick = function () {
        };
    }
}

function hideElement(element){
    element.style.visibility = "hidden";
    element.style.opacity = "0";
}

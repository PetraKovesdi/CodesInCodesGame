console.log("Hello, this is a console message.");

const STARTING_POSITION = 121212;

let position = STARTING_POSITION;
let step = "first";

function sendAdjustment(adjustment){
    let data = {
        "step": String(step),
        "position": String(position),
        "adjustment": String(adjustment)
    }

    fetchNextPos(data)

}

function fetchNextPos(data) {
    fetch('/ninth/api', {
    method: 'POST',
    mode: 'same-origin',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(res => {console.log("Data sent:", data); return res.json()})
        .then(respData => new Promise((resolve,reject) => {
            if (Object.keys(respData).includes("nextStep")
                && Object.keys(respData).includes("currentPosition")) {
                step = respData["nextStep"];
                position = step != "first" ? respData["currentPosition"] : STARTING_POSITION;
                resolve(respData);
            } else {
                step = "first";
                position = STARTING_POSITION;
                reject(respData);
            }
        }))
        .then((respData) => console.log("Response received:", respData))
        .catch((data) => console.log("Error in communication:", data))

}


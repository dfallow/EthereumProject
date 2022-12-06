const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const registerButton = document.querySelector(".register-button");
const filesUploaded = document.querySelector("#file");
const transferButton = document.querySelector(".transfer-button");
const doctorAddress = document.querySelector("#doctor-address");
const transferDiv = document.querySelector(".transfer-div");
const registerDiv = document.querySelector(".register-div");
// const inputText = document.querySelector('.input-text');
// const connectButton = document.querySelector('.connect-button');

registerDiv.style.display = "block";
transferDiv.style.display = "none";

function uploadImage() {
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(filesUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log("https://ipfs.io/ipfs/" + path + "?" + path);

    const request = new XMLHttpRequest();
    request.open("POST", `/ProcessMachineInfo/${path}`);
    request.send();
    registerDiv.style.display = "none";
    transferDiv.style.display = "block";
  };
}

function transferOwnership() {
  const request = new XMLHttpRequest();
  request.open("POST", `/TransferMachineOwnership/${doctorAddress.value}`);
  request.send();
}

inputFile.onchange = function (evt) {
  var tgt = evt.target || window.event.srcElement,
    files = tgt.files;

  // FileReader support
  if (FileReader && files && files.length) {
    var fr = new FileReader();
    fr.onload = function () {
      document.querySelector(".image").src = fr.result;
    };
    fr.readAsDataURL(files[0]);
  }
  // Not supported
  else {
    console.log("File reader not supported");
  }
};

/* async function connectToMetamask() {
  if (typeof window.ethereum !== 'undefined') {
    ethereum.request({ method: 'eth_requestAccounts' });
  }
} */

registerButton.addEventListener("click", async () => {
  uploadImage();
});

transferButton.addEventListener("click", async () => {
  transferOwnership();
});

/* connectButton.addEventListener('click', () => {
  connectToMetamask();
});
 */

const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const registerButton = document.querySelector(".register-button");
const filesUploaded = document.querySelector("#file");
const transferButton = document.querySelector(".transfer-button");
const doctorAddress = document.querySelector("#doctor-address");
const transferDiv = document.querySelector(".transfer-div");
const registerDiv = document.querySelector(".register-div");
const loading = document.querySelector("#loading");

registerDiv.style.display = "block";
transferDiv.style.display = "none";
registerButton.style.display = "block";
loading.style.display = "none";

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
    loading.style.display = "none";
  };
}

function transferOwnership() {
  const request = new XMLHttpRequest();
  request.open("POST", `/TransferMachineOwnership/${doctorAddress.value}`);
  request.send();
}

registerButton.addEventListener("click", async () => {
  registerButton.style.display = "none";
  loading.style.display = "block";
  uploadImage();
});

transferButton.addEventListener("click", async () => {
  transferOwnership();
  window.history.back();
});

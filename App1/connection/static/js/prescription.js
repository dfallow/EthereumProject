const inputMachineID = document.querySelector("#machine-id");
const inputDoctorAddress = document.querySelector("#doctor-address");
const inputPatientAddress = document.querySelector("#patient-address");
const inputFile = document.querySelector(".input-file");
const issueButton = document.querySelector(".btn-issue");
const transferButton = document.querySelector(".btn-transfer");
const fileUploaded = document.querySelector("#file");
const transferDiv = document.querySelector(".transfer-div");
const issueDiv = document.querySelector(".issue-div");

transferDiv.style.display = "none";
issueDiv.style.display = "flex";

issueButton.addEventListener("click", async () => {
  uploadFile();
});

transferButton.addEventListener("click", async () => {
  transfer();
});

async function uploadFile() {
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(fileUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log("https://ipfs.io/ipfs/" + path + "?" + path);

    const allData = {
      image: path,
      machineTokenId: inputMachineID.value,
      patient: inputPatientAddress.value,
      doctor: inputDoctorAddress.value,
    };

    console.log("All Data", allData);
    const request = new XMLHttpRequest();
    request.open("POST", `/ProcessPrescription/${JSON.stringify(allData)}`);
    request.send();
    transferDiv.style.display = "flex";
    issueDiv.style.display = "none";
  };
}

async function transfer() {
  const allData = {
    machineTokenId: inputMachineID.value,
    patient: inputPatientAddress.value,
    doctor: inputDoctorAddress.value,
  };

  const request = new XMLHttpRequest();
  request.open("POST", `/TransferMachineToPatient/${JSON.stringify(allData)}`);
  request.send();
}

inputFile.onchange = function (evt) {
  var tgt = evt.target || window.event.srcElement,
    files = tgt.files;

  // FileReader support
  if (FileReader && files && files.length) {
    var fr = new FileReader();
    fr.onload = function () {
      document.querySelector(".file").src = fr.result;
    };
    fr.readAsDataURL(files[0]);
  }
  // Not supported
  else {
    console.log("File reader not supported");
  }
};

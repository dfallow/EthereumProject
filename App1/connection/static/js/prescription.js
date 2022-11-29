const inputMachineID = document.querySelector("#machine-id").value;
const inputDoctorAddress = document.querySelector("#doctor-address").value;
const inputPatientAddress = document.querySelector("#patient-address").value;
const inputFile = document.querySelector(".input-file");
const createButton = document.querySelector(".btn");
const filesUploaded = document.querySelector("#file");

createButton.addEventListener("click", async () => {
  uploadMultipleFiles();
});

async function uploadMultipleFiles() {
  const node = await Ipfs.create();

  const resultsArray = [];

  let fileArray = [];
  for (let i = 0; i < filesUploaded.files.length; i++) {
    const fileReader = new FileReader();
    fileReader.readAsArrayBuffer(filesUploaded.files[i]);

    fileReader.onload = async () => {
      let { path } = await node.add(fileReader.result);

      fileArray.push(path);

      console.log("FILE ARRAY", fileArray.toString());
      console.log("PATH", path);

      if (fileArray.length == filesUploaded.files.length) {
        console.log("EOFIHEFOIHEWFI");
        let allData = {
          image: fileArray.toString(),
          name: "FromMachine",
          attributes: [{ machine: inputMachineID }],
        };

        console.log("ALL DATA", allData);

        let request = new XMLHttpRequest();
        request.open(
          "POST",
          `/ProcessFilesInfo/${JSON.stringify(
            allData
          )}/${inputMachineID}/${inputPrescriptionID}/${inputDoctorAddress}/${inputPatientAddress}`
        );
        request.send();
      }
    };
  }

  console.log("RESULTS ARRAY", resultsArray);

}

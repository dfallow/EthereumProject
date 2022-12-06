const inputDoctorAddress = document.querySelector("#doctor-address");
const inputPatientAddress = document.querySelector("#patient-address");
const registerButton = document.querySelector(".btn");

registerButton.addEventListener("click", async () => {
  addData();
});

function addData() {
  const allData = {
    patient: inputPatientAddress.value,
    doctor: inputDoctorAddress.value,
  };

  console.log("All Data", allData);
  const request = new XMLHttpRequest();
  request.open("POST", `/ProcessPatient/${JSON.stringify(allData)}`);
  request.send();
}
const inputDoctorAddress = document.querySelector("#doctor-address");
const inputPatientAddress = document.querySelector("#patient-address");
const registerButton = document.querySelector(".btn");
const loading = document.querySelector("#loading");

loading.style.display = "none";
registerButton.style.display = "block";

registerButton.addEventListener("click", async () => {
  registerButton.style.display = "none";
  loading.style.display = "block";
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
  window.history.back();
}

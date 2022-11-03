const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const inputText = document.querySelector(".input-text");
const button = document.querySelector(".btn");
const fileName = document.querySelector("#name")

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

button.addEventListener("click", () => {
  const allData = {
    "name": fileName.value,
    "description": inputText.value
  }
  console.log("test", allData)
  //const inputInfo = inputText.value;
  const request = new XMLHttpRequest();
  request.open("POST", `/ProcessInfo/${JSON.stringify(allData)}`);
  request.send();
});

const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");

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

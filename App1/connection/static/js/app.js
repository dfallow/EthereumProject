const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const inputText = document.querySelector(".input-text");
const button = document.querySelector(".btn");
const machineName = document.querySelector("#name");
const machineDepartment = document.querySelector("#department");
const imageUploaded = document.querySelector("#file");

const machineId = "ThisWillBeAnAddress";
const resultsArray = "";

async function uploadMultipleFiles() {
  const node = await Ipfs.create();

    const resultsArray = [];
    
    let fileArray = [];
    for (let i=0; i<imageUploaded.files.length; i++) {
      const fileReader = new FileReader();
      fileReader.readAsArrayBuffer(imageUploaded.files[i]);

      fileReader.onload = async () =>  {
      
        let { path } = await node.add(fileReader.result);

        fileArray.push(path);

        console.log("FILE ARRAY", fileArray.toString());
        console.log("PATH", path);

        if ( fileArray.length == imageUploaded.files.length) {
          console.log("EOFIHEFOIHEWFI")
          let allData = {
            image: fileArray.toString(),
            name: "FromMachine",
            attributes: [{machine: machineId}]
          };
        
          console.log("ALL DATA", allData);
        
          let request = new XMLHttpRequest();
          request.open("POST", `/ProcessInfo/${JSON.stringify(allData)}`)
          request.send();
        }
       }
    }

  
  console.log("RESULTS ARRAY", resultsArray)

  
  //window.location.reload();

}

async function sendToPython() {
  console.log("Before");
  let test = await uploadMultipleFiles();
  console.log("After");
  console.log("PROMISE", test);
  console.log("After After");
}

function uploadImage() {
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(imageUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log("https://ipfs.io/ipfs/" + path + "?" + path);

    const allData = {
      image: path,
      name: machineName.value,
      attributes: [{ department: machineDepartment.value }],
    };

    console.log("test", allData);
    const request = new XMLHttpRequest();
    request.open("POST", `/ProcessInfo/${JSON.stringify(allData)}`);
    request.send();
    window.location.reload();
  };
}

// inputFile.onchange = function (evt) {
//   var tgt = evt.target || window.event.srcElement,
//     files = tgt.files;

//   // FileReader support
//   if (FileReader && files && files.length) {
//     var fr = new FileReader();
//     fr.onload = function () {
//       document.querySelector(".image").src = fr.result;
//     };
//     fr.readAsDataURL(files[0]);
//   }
//   // Not supported
//   else {
//     console.log("File reader not supported");
//   }
// };

function checkDir() {
  console.log("here");
  //var check = document.getElementById("fileToUpload").value;
  let check = imageUploaded.value
  console.log("TEST", check);
  const arr = check.split("\\");
  console.log(arr);
  console.log("Is this your folder : " , arr.at(arr.length -1) );
  console.log(check);
}

button.addEventListener("click", async () => {
  // uploadImage();
  uploadMultipleFiles();
  //sendToPython();
  //checkDir();
});
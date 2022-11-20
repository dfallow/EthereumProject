const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const inputText = document.querySelector(".input-text");
const button = document.querySelector(".btn");
const machineName = document.querySelector("#name");
const machineDepartment = document.querySelector("#department");
const imageUploaded = document.querySelector("#file");

async function uploadFiles() {
  const node = await Ipfs.create();
  const resultArr = [];
  const fileArray = Array.from(imageUploaded.files);
  const dirResult = [];

  let fileObjectArray = fileArray.map((file) => {
    return {
      path: file.name,
      content: file,
    };
  });

  for await (const file of node.addAll(fileObjectArray, {
    wrapWithDirectory: true,
  })) {
    resultArr.push(file);
  }

  const directoryCID = resultArr[resultArr.length - 1].cid;

  for await (const item of node.ls(directoryCID)) {
    dirResult.push(item);
  }

  console.log("dirResult", dirResult);

  const allData = [];

  const directory = dirResult[0]["path"].split("/")[0];
  console.log("dir", directory);

  for (let i = 0; i < dirResult.length; i++) {
    const fileData = {
      directory: directory,
      name: dirResult[i].name,
      attributes: [
        { machineName: machineName.value },
        { department: machineDepartment.value },
      ],
    };
    allData.push(fileData);
  }

  console.log("test", allData);
  const request = new XMLHttpRequest();
  request.open("POST", `/ProcessInfo/${JSON.stringify(allData)}`);
  request.send();
  window.location.reload();
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

button.addEventListener("click", async () => {
  //uploadImage();
  uploadFiles();
});

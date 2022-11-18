const image = document.querySelector(".image");
const inputFile = document.querySelector(".input-file");
const inputText = document.querySelector(".input-text");
const button = document.querySelector(".btn");
const machineName = document.querySelector("#name");
const machineDepartment = document.querySelector("#department");
const imageUploaded = document.querySelector("#file");

function uploadImage2() {
  return new Promise((resolve) => {
    const ipfs__files = [];

    for (let i = 0; i < imageUploaded.files.length; i++) {
      console.log(i);
        ipfs__files.push(addFile(i))
    }

    setTimeout(() => {
      console.log("HERE", ipfs__files);
      return resolve(ipfs__files);
    }, 20000)
  })
}

async function createDir() {
  const node = await Ipfs.create()
  const resultArr = [];
  //const node = await Ipfs.create({ repo: nodeId});

  //console.log("NODE", nodeId)
  //window.Node = node;
  //const status = node.isOnline() ? 'online' : 'offline'
  //console.log(`Node Status: ${status}`)

  //var loc = window.location.pathname;
  //  var dir = loc.substring(0, loc.lastIndexOf('/'));
  //  let { path } = await node.add(dir);

  //let dir = await node.files.mkdir("/myNewNewDir");
  
  //console.log("DIRECTORY", await dir);


  const fileArray = Array.from(imageUploaded.files)

  const filesWithPath = [];
  for (let i=0; i<fileArray.length; i++) {
    let object = {
      path: `${fileArray[i].name}`,
      content: fileArray[i]
    }
    filesWithPath.push(object);
  }

  console.log("NEW ARRAY", filesWithPath);

  let result = await node.add(imageUploaded.files[0]);

  console.log("SINGLE FILE RESULT", result);
  console.log("https://ipfs.io/ipfs/" + result.path + "?" + result.path);
  //let { result } = await node.addAll(filesWithPath)
  for await (const result of node.addAll(filesWithPath, { 
    
  })) {
    console.log("SINGLE RESULT", result)
  }

  //console.log("NEW RESULTS", await result)

  // for (let i=0; i<imageUploaded.files.length; i++) {


  //   let result = node.add(imageUploaded.files[i])
  //   console.log("RESULT", await result);
  //   resultArr.push(await result);

  // }
  // console.log("RESULT ARRAY", resultArr);

  // console.log("RESULT ARRAY", resultArr[0].path);

  // console.log(imageUploaded.files);
  // for await (const result of node.addAll([imageUploaded.files[0], imageUploaded.files[1]])) {
  //   var loc = window.location.pathname;
  //   var dir = loc.substring(0, loc.lastIndexOf('/'));
  //   let { path } = await node.add(dir);
  //   console.log(path)
  //   console.log("https://ipfs.io/ipfs/" + path + "?" + path);
  // }
}


function uploadImage() {
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(imageUploaded.files[index]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    var loc = window.location.pathname;
    var dir = loc.substring(0, loc.lastIndexOf('/'));
    let { path } = await node.add(dir);
    console.log("PATH", path);

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
  console.log(imageUploaded.files);
  createDir();
  
  
});
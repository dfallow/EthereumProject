const inputMachineID = document.querySelector('#machine-id');
const inputFile = document.querySelector('.input-file');
const button = document.querySelector('.btn');
const filesUploaded = document.querySelector('#file');

button.addEventListener('click', async () => {
  uploadData();
});

function uploadData() {
  console.log(filesUploaded.files);
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(filesUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log('https://ipfs.io/ipfs/' + path + '?' + path);

    const allData = {
      image: path,
      name: machineName.value,
      attributes: [{ department: machineDepartment.value }],
    };

    console.log('test', allData);

    const request = new XMLHttpRequest();
    request.open('POST', `/ProcessInfo/${JSON.stringify(allData)}`);
    request.send();
    window.location.reload();
  };
}

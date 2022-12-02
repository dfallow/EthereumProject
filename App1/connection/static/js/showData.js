const generateButton = document.querySelector('.generate-button');

generateButton.addEventListener('click', generatePlots);

function generatePlots() {
  const request = new XMLHttpRequest();
  request.open('GET', `/ProcessPlotsInfo`);
  request.send();
}

const colorChangeButton = document.getElementById('but');

function changeBodyColor() {
    // Generate a random color (optional, you can use a fixed color)
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);

    // Set the body's background color
    document.body.style.backgroundColor = randomColor;
}
// Add an event listener to the button
colorChangeButton.addEventListener('click', changeBodyColor);


// iniciar gravação no servidor
document.getElementById('start-recording').addEventListener('click', async () => {
  await fetch('/start', { method: 'POST' });
});

// se quiser forçar reload do preview depois:
document.getElementById('video').src = '/video?ts=' + Date.now();



// parar gravação no servidor
document.getElementById('stop-recording').addEventListener('click', async () => {
  await fetch('/stop', { method: 'POST' });
});

// se quiser forçar reload do preview depois:
document.getElementById('video').src = '/video?ts=' + Date.now();
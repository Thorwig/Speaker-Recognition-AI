navigator
    .mediaDevices
    .getUserMedia({audio: true})
    .then(stream => { handlerFunction(stream) });

function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive") {
            let blob = new Blob(audioChunks, {type: 'audio/mpeg-3'});
            sendData(blob);
        }
    }
}
//Send data to backend
function sendData(data) {
    var form = new FormData();
    form.append('file', data, 'data.mp3');
    form.append('title', 'data.mp3');
    form.append('firstname', firstname.value);
    form.append('lastname', lastname.value);

    $.ajax({
        type: 'POST',
        url: '/enroll',
        data: form,
        cache: false,
        processData: false,
        contentType: false
    }).done(function(data) {
        console.log(data);
        enroll_output.innerHTML="The audio has been enrolled successfully !"

    });
}

//Start recording button 
startRecording.onclick = e => {
    startRecording.disabled = true;
    firstname.disabled = true;
    lastname.disabled = true;
    setTimeout(() => { document.getElementById("startRecording").style.display = "none"; document.getElementById("stopRecording").style.display = "inherit"; stopRecording.disabled = false; }, 4000);
    audioChunks = [];
    verify_output.innerHTML ="Recording..."
    rec.start();
};

//Stop recording button 
stopRecording.onclick = e => {
    verify_output.innerHTML =" "
    startRecording.disabled = true;
    stopRecording.disabled = true;
    document.getElementById("startRecording").style.display = "inherit"; 
    document.getElementById("stopRecording").style.display = "none";
    rec.stop();
};

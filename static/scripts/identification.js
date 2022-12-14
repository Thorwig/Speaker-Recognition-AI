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

    if(hidden_input.value != ''){
        form.append('audioname', hidden_input.value);
    }

    $.ajax({
        type: 'POST',
        url: '/identify',
        data: form,
        cache: false,
        processData: false,
        contentType: false
    }).done(function(data) {
        console.log(data);
        console.log(hidden_input.value);
        if(hidden_input.value=='audio2'){
            verify_output.innerHTML='First name : '+data['first_name']+', Last name : '+data['last_name'] +', Score : '+data['score']
            verify_output1.innerHTML='First name : '+data['first_name1']+', Last name : '+data['last_name1'] +', Score : '+data['score1']
            verify_output2.innerHTML='First name : '+data['first_name2']+', Last name : '+data['last_name2'] +', Score : '+data['score2']
        }

    });
}

//Start recording button 
startRecording_.onclick = e => {
    hidden_input.value = 'audio2';
    startRecording_.disabled = true;
    setTimeout(() => { document.getElementById("startRecording_").style.display = "none"; document.getElementById("stopRecording_").style.display = "inherit"; stopRecording_.disabled = false; }, 4000);
    audioChunks = [];
    verify_output.innerHTML ="Recording..."
    rec.start();
    
};

//Stop recording button 
stopRecording_.onclick = e => {
    verify_output.innerHTML =" ";
    hidden_input.value = 'audio2';
    stopRecording_.disabled = true;
    setTimeout(() => { document.getElementById("startRecording_").style.display = "inherit"; 
    document.getElementById("stopRecording_").style.display = "none"; startRecording_.disabled = false; }, 3000);
    rec.stop();
};

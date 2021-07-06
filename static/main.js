
var endPoint = '';
var loc = window.location;
var wsStart = 'ws://';
if(loc.protocol == 'https:'){
    wsStart = 'wss://';
}
var endPoint = wsStart + loc.host + loc.pathname;

var webSocket;
webSocket = new WebSocket(endPoint);

webSocket.onopen = function(e){
    console.log('Connection opened! ', e);
}

webSocket.onmessage = webSocketOnMessage;

webSocket.onclose = function(e){
    console.log('Connection closed! ', e);
}

webSocket.onerror = function(e){
    console.log('Error occured! ', e);
}
function webSocketOnMessage(event){
    var parsedData = JSON.parse(event.data);

    var action = parsedData['action'];
    
    console.log('action: ', action);
    var receiver_channel_name = parsedData['message']['receiver_channel_name'];
    console.log('receiver_channel_name: ', receiver_channel_name);

    // in case of new peer
    if(action == 'new-peer'){
        console.log('New peer: ', peerUsername);

        // create new RTCPeerConnection
        createOfferer(receiver_channel_name);

    
    }
}
const localVideo = document.querySelector('#local-video');
var localStream = new MediaStream();
btnToggleAudio = document.querySelector("#audio_btn");
btnToggleVideo = document.querySelector("#video_btn");

const constraints = {
    'video': true,
    'audio': true
}
userMedia = navigator.mediaDevices.getUserMedia(constraints)
    .then(stream => {
        localStream = stream;
        console.log('Got MediaStream:', stream);
        localVideo.srcObject = localStream;
        localVideo.muted = true;
    })
        // window.stream = stream; // make variable available to browser console
    .catch(error => {
        console.log('Error accessing display media.', error);
    });

    function sendSignal(action, message){
        webSocket.send(
            JSON.stringify(
                {
                    'action': action,
                    'message': message,
                }
            )
        )
    }
    var configuration = {
        'iceServers': [{
            "urls": ["stun:stun1.l.google.com:19302", 
            "stun:stun.l.google.com:19302",
            "stun:stun2.l.google.com:19302"]
        }]
    };
    function createOfferer(receiver_channel_name){
        var peer = new RTCPeerConnection(configuration);
    }
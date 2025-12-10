//display speak message in the web app
$(document).ready(function () {



eel.expose(DisplayMessage);
function DisplayMessage(message){
   
    $('.siri-message').text(message);
    $('.siri-message').textillate('start');



}
//display hood
eel.expose(Showhood)
function Showhood(){
    $('#oval').attr("hidden", false);
    $('#SiriWave').attr("hidden", true);
}

//chatbox send message
eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
    }
    




      


}
);


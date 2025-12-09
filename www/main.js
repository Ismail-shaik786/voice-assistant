

$(document).ready(function () {
    $('.text2').textillate({
        loop: true,
        sync: true,
        in:{
            effect:'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        },
    });
    //SiriWave
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: 'ios9',
    amplitude: '1',
    autostart: true,
    speed:0.30
   
  });
    //sirimessage animation
     $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect:'bounceIn',
            sync:true,
        },
        out: {
            effect: 'bounceOut',
            sync:true,
        },
    });
    //micbutton 
    $('#MicBtn').click(function(){
        eel.playAssistancesound();
        $('#oval').attr("hidden", true);
        $('#SiriWave').attr("hidden", false);
        eel.allCommands()();
    });
//shortcut key
    function doc_keyUp(e) {
        if(e.key =="j" && e.metaKey){
            eel.playAssistancesound();
            $('#oval').attr("hidden", true);
            $('#SiriWave').attr("hidden", false);
            eel.allCommands()();
    }

}
document.addEventListener('keyup', doc_keyUp, false);
 //send button


function playAssistant(message){
    if(message !=""){
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands(message);
        $('#chatbox').val("")
        $('#MicBtn').attr('hidden', false);
        $('#SendBtn').attr('hidden', true);
    }
 }
function ShowHideButton(message){
    if(message.length ==0){
        $('#MicBtn').attr('hidden', false);
        $('#SendBtn').attr('hidden', true);
    }
    else{
        $('#MicBtn').attr('hidden', true);
        $('#SendBtn').attr('hidden', false);
 }
}
$("#chatbox").keyup(function(){
    let message=$("#chatbox").val();
    ShowHideButton(message);
});
$('#SendBtn').click(function(){
    let message=$("#chatbox").val();
    eel.playAssistancesound();
    playAssistant(message);
});
$('#chatbox').keypress(function (e) {
    key=e.which;
    if (e.which == 13) {
        let message=$("#chatbox").val();
        eel.playAssistancesound();
        playAssistant(message);
    }
});

});
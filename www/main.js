

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
//stopiing assitant
// Stop setting button
// OPEN SETTINGS PANEL
$("#SettingBtn").click(function () {
    $("#settings-panel").removeAttr("hidden");
});

// CLOSE SETTINGS PANEL
$("#close-settings").click(function () {
    $("#settings-panel").attr("hidden", true);
});

// TAB SWITCHING
$(".tab-btn").click(function () {
    let tab = $(this).data("tab");

    $(".tab-btn").removeClass("active");
    $(this).addClass("active");

    $(".tab-content").removeClass("active");
    $("#" + tab).addClass("active");
});

//setting panel control
// TAB 1 — CONTACT DETAILS
$("#tab1 .add-btn").click(function () {
    let name = $("#contact-name").val().trim();
    let number = $("#contact-number").val().trim();

    if (name === "" || number === "") {
        alert("Please fill all fields");
        return;
    }

    eel.insert_contact(name, number)(function (response) {
        alert(response);
        $("#contact-name").val("");
        $("#contact-number").val("");
    });
});

// TAB 2 — WEBPAGE DETAILS
$("#tab2 .add-btn").click(function () {
    let webName = $("#web-name").val().trim();
    let webPath = $("#web-path").val().trim();

    if (webName === "" || webPath === "") {
        alert("Please fill all fields");
        return;
    }

    eel.insert_webpage(webName, webPath)(function (response) {
        alert(response);
        $("#web-name").val("");
        $("#web-path").val("");
    });
});

// TAB 3 — SYSTEM APPS
$("#tab3 .add-btn").click(function () {
    let appName = $("#app-name").val().trim();
    let appPath = $("#app-path").val().trim();

    if (appName === "" || appPath === "") {
        alert("Please fill all fields");
        return;
    }

    eel.insert_app(appName, appPath)(function (response) {
        alert(response);
        $("#app-name").val("");
        $("#app-path").val("");
    });
});
//detele from setting panel
$("#tab1 .add-btn2").click(function () {
    let name = $("#contact-name").val().trim();
    let number = $("#contact-number").val().trim();

    if (name === "" || number === "") {
        alert("Please fill all fields");
        return;
    }

    eel.delete_contact(name, number)(function (response) {
        alert(response);
        $("#contact-name").val("");
        $("#contact-number").val("");
    });
});

// TAB 2 — WEBPAGE DETAILS
$("#tab2 .add-btn2").click(function () {
    let webName = $("#web-name").val().trim();
    let webPath = $("#web-path").val().trim();

    if (webName === "" || webPath === "") {
        alert("Please fill all fields");
        return;
    }

    eel.delete_webpage(webName, webPath)(function (response) {
        alert(response);
        $("#web-name").val("");
        $("#web-path").val("");
    });
});

// TAB 3 — SYSTEM APPS
$("#tab3 .add-btn2").click(function () {
    let appName = $("#app-name").val().trim();
    let appPath = $("#app-path").val().trim();

    if (appName === "" || appPath === "") {
        alert("Please fill all fields");
        return;
    }

    eel.delete_app(appName, appPath)(function (response) {
        alert(response);
        $("#app-name").val("");
        $("#app-path").val("");
    });
});
//stop siri
$(document).ready(function () {

    // When any key is pressed
    $(document).on("keydown", function (e) {

        // Switch SiriWave -> Oval
        $("#SiriWave").attr("hidden", true);
        $("#Oval").attr("hidden", false);

        // Stop assistant speaking (your existing stop function)
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }

        console.log("Key pressed, assistant stopped.");
    });

});
$("#tab4 .add-btn").click(function () {
    let api = $("#api_key").val().trim();
    

    if (api === "" ) {
        alert("Please fill all fields");
        return;
    }

    eel.addApi(api)(function (response) {
        alert(response);
        $("#api_key").val("");
        
    });
});



});

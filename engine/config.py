import eel
ASSISTANCE_NAME="root"
system_apps={
    "whatsapp":'C:\\Users\\ISMAIL\\OneDrive\\Desktop\\Whatsapp.lnk',
    "chrome":'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    "edge":'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    "vlc":'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe',
    
    "visual studio code":'C:\\Users\\ISMAIL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    "oracle virtualbox":'C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'

}
web_apps={
    "youtube":'https://www.youtube.com',
    "facebook":'https://www.facebook.com',
    "gmail":'https://mail.google.com',
    "google":'https://www.google.com',
    "chatgpt":'https://chat.openai.com/'
}
contacts = {
    "Gane": "+917095501460",
    "Unknown": "+918744814207",
    "Tickets Hall": "222-613-1324",
    "AL hello tunes": "543-211",
    "emergency hotline": "55100",
    "My Id": "+913325090377",
    "railway inquiry": "139",
    "ITSir": "+919703244455",
    "Kala Mam Iiit 2": "+917649836481",
    "Karimun2": "+917702766130",
    "Kotesvar Clg": "+919676508130",
    "instant help 24x7": "121",
    "airtel live": "54321",
    "Mk3": "905-251-4710",
    "Mohan Krishna Frd": "+919052514710",
    "My  New": "+918184918441",
    "sravya": "+916302625022",
    "Bhatraju Sir": "+919666762604",
    "Adithya Cse Iiit": "+919392303243",
    "Subhani Va": "+919347909809",
    "Prasad Iiit": "+917672074431",
    "Vaasu Sir": "995-955-2795",
    "Karthik Cse Iiit": "+919347891809",
    "Sameer Iiit": "+918919027737",
    "Police": "100",
    "Ambulance": "102",
    "Jio Plan & Offers": "1991",
    "Hello Jio": "1234",
    "Jio Care": "199",
    "Ashok 10 Th": "+916304117930",
    "Aunty(giri )": "+918897438990",
    "Gundu": "+919912937243",
    'manohar':'+917981972986',
    'phani':"+918688085352",
    "potti":'+918688125417'
}


#

@eel.expose
def save_contact(name, number):
    contacts[name] = number
    return f"Contact saved: {name} - {number}"

@eel.expose
def save_webpage(webName, webPath):
    web_apps[webName] = webPath
    return f"Webpage saved: {webName}"

@eel.expose
def save_app(appName, appPath):
    system_apps[appName] = appPath
    return f"App saved: {appName}"

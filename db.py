import sqlite3
import eel
def connect_db():
    return sqlite3.connect("config.db")



    

# ------------------------------------
# INSERT FUNCTIONS
# ------------------------------------
@eel.expose
def insert_contact(name, number):
 try:
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    db.commit()
    db.close()
    return f"Contact saved: {name} - {number}"
 except Exception as e:
        print("ERROR in insert_contact:", e)
        return "Error occurred"

@eel.expose
def insert_webpage(name, path):
 try:
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO webpages (web_name, web_path) VALUES (?, ?)", (name, path))
    db.commit()
    db.close()
    return f"Webpage saved for: {name}"
 except Exception as e:
        print("ERROR in insert_webpage:", e)
        return "Error occurred"

@eel.expose
def insert_app(name, path):
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO system_apps (app_name, app_path) VALUES (?, ?)", (name, path))
        db.commit()
        db.close()
        return f"App saved: {name}"
    except Exception as e:
        print("ERROR in insert_apps:", e)
        return "Error occurred"
#------------------------------------
# delete FUNCTIONS
# ------------------------------------
@eel.expose
def delete_contact(name, number):
 try:
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM contacts WHERE name=? AND  number=?", (name, number))
    db.commit()
    
    if cursor.rowcount >0:
        db.close()
        return f"Contact deleted: {name} - {number}"
    else:
        db.close()
        return f"There is no data about {name}"
 except Exception as e:
        print("ERROR in insert_contact:", e)
        return "Error occurred"

@eel.expose
def delete_webpage(name, path):
 try:
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM webpages WHERE web_name = ? AND web_path=? ", (name,path))
    db.commit()
    if cursor.rowcount >0:
        db.close()
        return f"Webpage details deleted : {name}:{path}"
    else:
        db.close()
        return f"There is no data about {name}"
    
 except Exception as e:
        print("ERROR in insert_webpage:", e)
        return "Error occurred"

@eel.expose
def delete_app(name, path):
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM system_apps WHERE app_name = ?  AND app_path=?", (name,path))
        db.commit()
        if cursor.rowcount >0:
            db.close()
            return f"{name}infromation is deleted .path  :  {path}"
        else:
            return f"There is no data about {name}"
        
    except Exception as e:
        print("ERROR in insert_apps:", e)
        return "Error occurred"
# apki key
@eel.expose
def addApi(api):
 try:
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT or replace INTO Apikey (id, value) VALUES (1, ?)",(api,))

    db.commit()
    if cursor.rowcount >0:
        db.close()
        return f"APIKEY is saved as: {api}"
    else:
        db.close()
        return "insertion failed "
  
 except Exception as e:
        print("ERROR in addApi:", e)
        return "Error occurred"

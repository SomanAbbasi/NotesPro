import sqlite3

def init_db():
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )    
        """)
    conn.commit()
    conn.close()

def get_all_notes():
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("SELECT * FROM notes")
    notes=c.fetchall()
    conn.close()   
    return notes
    
    
def get_single_note(note_id):
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("SELECT * FROM notes WHERE id=?",(note_id,))
    note=c.fetchone()
    conn.close()
    return note
    
def add_note(title,content):
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("INSERT INTO notes (title,content) VALUES (?,?)",(title,content))
    conn.commit()
    conn.close()
    
def delete_note(note_id):
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?",(note_id,))
    conn.commit()
    conn.close()
        
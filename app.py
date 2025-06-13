from flask import Flask,request,jsonify,render_template,redirect,url_for
import database

app=Flask(__name__)
#Create database.db
database.init_db()


# @app.route('/')
# def home():
#     return "Flask API is running!"

@app.route('/api/notes',methods=['GET'])
def api_get_notes():
    notes=database.get_all_notes()
    return jsonify(notes)

@app.route('/api/notes/<int:note_id>',methods=['GET'])
def api_get_note(note_id):
    note=database.get_single_note()
    if note:
        return jsonify(note)
    return jsonify({"error":"Note not found."}),404

@app.route('/api/notes',methods=['POST'])
def api_add_note():
    data=request.get_json()
    title=data.get('title')
    content=data.get('content')
    if not title or not content:
        return jsonify({"error":"Missing Data"}),400
    database.add_note(title,content)
    return jsonify({'message':'Note added successfully!'})

@app.route('/api/notes/<int:note_id>',methods=['DELETE'])
def api_delete_note(note_id):
    database.delete_note(note_id)
    return jsonify({'message':'Note deleted successfully!'})

#Web Routes
@app.route('/')
def index():
    notes=database.get_all_notes()
    return render_template("index.html",notes=notes)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']
        if title and content:
            database.add_note(title,content)
            return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete(note_id):
    database.delete_note(note_id)
    return redirect(url_for('index'))

    
if __name__=="__main__":
    app.run(debug=True)
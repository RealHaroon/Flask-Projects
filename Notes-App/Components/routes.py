from flask import render_template,request,redirect,url_for,flash
from Components import app
from Components.models import Note,db



@app.route('/')
def index():
    notes = Note.query.order_by(Note.updated_at.desc()).all()
    return render_template('index.html', notes=notes)


@app.route('/',methods=['POST'])
def  add_note():
    title=request.form['title']
    content=request.form['content']


    if not title or not content:
        flash('Title and Content cannot be empty!',category='warning')
        return  redirect(url_for('index'))


    newNote=Note(title=title,content=content)
    db.session.add(newNote)
    db.session.commit()
    flash('Note Added Successfully!',category='success')
    return redirect(url_for('index'))


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit_note(id):
    note=Note.query.get_or_404(id)
    if  request.method  =='POST':
        note.title=request.form['title']
        note.content=request.form['content']
        db.session.commit()
        flash('Note  updated  successfully!',category='success')
        return redirect(url_for('index'))
    return render_template('index.html',edit_note=note,notes=Note.query.all())
    

@app.route('/delete/<int:id>')
def delete_note(id):
    note  = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash('Note Deleted Successfully!',category='success')
    return redirect(url_for('index'))

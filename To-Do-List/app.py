from flask import Flask,render_template,request,redirect,url_for,flash     #type:ignore
from models import db,Task


app=Flask(__name__)
app.secret_key='haroon-secret-123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# create table inside database ( once )
with app.app_context():
    db.create_all()



@app.route('/',methods=['GET','POST'])
def home():
   if request.method=='POST':
        text_task=request.form['task']
        if text_task:
           new_task=Task(task=text_task)
           db.session.add(new_task)
           db.session.commit()
        return redirect(url_for('home'))
   
   tasks=Task.query.all()
   return render_template('index.html',tasks=tasks)

@app.route('/done/<int:id>')
def mark_done(id):
    task=Task.query.get(id)
    if task:
        task.done=True
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    task=Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)



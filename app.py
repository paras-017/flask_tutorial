from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.app_context().push()
db = SQLAlchemy(app)



# Schema
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:      #The  purpose of __repr__ is to provide a helpful and unambiguous representation of an object for debugging purposes
        return f"{self.sno} - {self.title}"

#creating the database
db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def hello():
   #accepting data from UI
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        print(title, description)

        # creating a todo
        todo = Todo(title = title, description = description)
        # adding the todo to the database
        db.session.add(todo)
        db.session.commit()

    #getting all the todos from DB & sending them to the frontend
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)

@app.route('/show')
def show():
    # allTodo = Todo.query.all()
    # print(allTodo)
    return 'This is a product page'

@app.route('/edit/<int:sno>', methods = ['GET','POST'])
def edit(sno):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        todo = Todo.query.filter_by(sno = sno).first() 
        todo.title = title
        todo.description = description
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html', todo = todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

# if __name__ == '__main__':    
app.run(debug = True)
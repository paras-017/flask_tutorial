from flask import Flask, render_template
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
db.create_all()

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/products')
def products():
    return 'This is a product page'

# if __name__ == '__main__':    
app.run(debug = True)
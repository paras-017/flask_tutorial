from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/products')
def products():
    return 'This is a product page'

if __name__ == '__main__':    
    app.run(debug = True)
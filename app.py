from flask import Flask, render_template, request
from emailpy import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/validate', methods=['POST'])
def validate():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    domin = request.form['domin']
    email = run(firstname, lastname, domin)
    send = f'The delivarible Email Address of the person is {email}'
    return render_template('index.html', email=send)

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask
app = Flask(_name_)
app.debug = True

@app.route('/hello/<Cyrus>')
def hello_name(Cyrus):
        return 'Hello %s!' % Cyrus

if _name_ == '_main_':
        app.ru

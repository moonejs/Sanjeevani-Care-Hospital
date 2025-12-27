from flask import Flask
from config import Config
from extensions import db

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(db)


@app.route('/')
def hello_world():
    return "<h1>Hello Mad-2</h1>"

if __name__=='__main__':
    app.run(debug=True)

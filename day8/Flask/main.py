from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "welcome"

@app.route("/read/<id>/")
def read(id):
    return f"Read {id}"

if __name__=='__main__':
    app.run(debug=True)
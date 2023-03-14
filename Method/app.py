import os
from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__ , template_folder=os.getcwd()+"\Web")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
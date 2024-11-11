from flask import Flask

app = Flask(__name__, template_folder="views")

@app.route("/")
def ferret_sound():
    pass
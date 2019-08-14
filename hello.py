from flask import Flask,render_template
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello Flask, on Azure App Service for Linux"

@myapp.route("/a")
def aa():
    return "12123Hello Flask, on Azure App Service for Linux"

@myapp.route("/shobhit")
def shobhit():
    return render_template("home.html")
# if __name__ == "__main__":
#     myapp.run(debug=True)
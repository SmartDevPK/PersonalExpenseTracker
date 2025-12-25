from flask import Flask, render_template
from app.api.user_routes import user_api

app = Flask(__name__)
app.register_blueprint(user_api)  

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

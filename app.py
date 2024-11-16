from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form.get("name_input")
        return render_template("greet.html", name=username)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


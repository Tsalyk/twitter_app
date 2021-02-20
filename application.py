from flask import Flask, render_template, request
from create_map import launch
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def register():
    nickname = request.form.get("nick")
    launch(nickname)

    if not request.form.get("nick"):
        return render_template("failure.html")
    return render_template("webmap.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=1010)
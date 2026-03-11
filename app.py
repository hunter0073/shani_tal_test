from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    """Serve logo images and any other static assets."""
    return send_from_directory(".", filename)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, redirect, render_template, request, send_file

app = Flask(__name__)
file_path = "downloads/DataWareHouse.pdf"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/redirect", methods=["GET", "POST"])
def google_redirect():
    return redirect("https://github.com/Buuchezo/BMI-Calculator")


@app.route("/download")
def download():
    return send_file(file_path, as_attachment=True, download_name="Lebenslauf.pdf")


if __name__ == "__main__":
    app.run(debug=True)

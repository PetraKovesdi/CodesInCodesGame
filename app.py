from flask import Flask, render_template, request, redirect, session
import util

app = Flask(__name__)
app.secret_key = b'19+M?W38;6S9N9=g|31NKm5xS'


@app.route('/', methods=["GET", "POST"])
@app.route('/first', methods=["GET", "POST"])
def first_page():
    if request.method == "GET":
        return render_template("startpoint.html")
    elif request.method == "POST":
        code = request.form.get("first")
        if util.verify_code(code, util.gethashes("first")):
            session["reached"] = 2
            return redirect("/second")
        else:
            return render_template("startpoint.html", message="Not correct, the 6-digit number is something else.")


@app.route('/second', methods=["GET", "POST"])
def second_page():
    if request.method == "GET":
        if "reached" in session and session["reached"] > 1:
            return "This page is under development."
        else:
            return redirect("/")
    if request.method == "POST":
        return redirect("/")



if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, redirect, session
import util

app = Flask(__name__)
app.secret_key = b'19+M?W38;6S9N9=g|31NKm5xS'

# First is not in PAGEMAP as it is also the root page
PAGEMAP = {
    "second": {"session": 2, "nextPage": "third", "code": util.HASHES["second"]},
    "third": {"session": 3, "nextPage": "fourth", "code": util.HASHES["third"]},
    "fourth": {"session": 4, "nextPage": "fifth", "code": util.HASHES["fourth"]},
    "fifth": {"session": 5, "nextPage": "notcomplete", "code": util.HASHES["fifth"]}
}


@app.route('/', methods=["GET", "POST"])
@app.route('/first', methods=["GET", "POST"])
def first_page():
    if request.method == "GET":
        return render_template("startpoint.html")
    elif request.method == "POST":
        if "first" in request.form:
            code = request.form.get("first")
            if util.verify_code(code, util.gethashes("first")):
                # if reached is already in session, it will not decrease it to 2
                if "reached" not in session:
                    session["reached"] = 2
                return redirect("/second")
        return render_template("startpoint.html", message="Not correct, the 6-digit number is something else.")


@app.route('/<page>', methods=["GET", "POST"])
def second_page(page):
    if request.method == "GET":
        if page in PAGEMAP \
                and "reached" in session \
                and session["reached"] >= PAGEMAP.get(page).get("session"):

            return f"{page} page is under development."
        else:
            return redirect("/")

    if request.method == "POST":
        return redirect("/")


if __name__ == '__main__':
    app.run()

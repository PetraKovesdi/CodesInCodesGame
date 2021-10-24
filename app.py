from flask import Flask, render_template, request, redirect, session, jsonify
import util
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'19+M?W38;6S9N9=g|31NKm5xS'

# First is not in PAGEMAP as it is also the root page
PAGEMAP = {
    "second": {"session": 2, "nextPage": "third", "code": util.HASHES["second"]},
    "third": {"session": 3, "nextPage": "fourth", "code": util.HASHES["third"]},
    "fourth": {"session": 4, "nextPage": "fifth", "code": util.HASHES["fourth"]},
    "fifth": {"session": 5, "nextPage": "sixth", "code": util.HASHES["fifth"]},
    "sixth": {"session": 6, "nextPage": "seventh", "code": util.HASHES["sixth"]},
    "seventh": {"session": 7, "nextPage": "eighth", "code": util.HASHES["seventh"]},
    "eighth": {"session": 8, "nextPage": "ninth", "code": util.HASHES["eighth"]},
    "ninth": {"session": 9, "nextPage": "tenth", "code": util.HASHES["eighth"]},
    "tenth": {"session": 10, "nextPage": "notComplete", "code": ""}
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
def mapped_page(page):
    # Both for GET and POST requests
    if page not in PAGEMAP \
                or "reached" not in session \
                or session["reached"] < PAGEMAP.get(page).get("session"):
        return redirect("/")

    if request.method == "GET":
        return render_template(f"{page}.html")

    if request.method == "POST":
        if page in request.form:
            code = request.form.get(page)
            if util.verify_code(code, util.gethashes(page)):
                # if higher number is already in session, it will not decrease it to prev number
                if session["reached"] == PAGEMAP.get(page).get("session"):
                    session["reached"] += 1
                return redirect(f"/{PAGEMAP.get(page).get('nextPage')}")
        return render_template(f"{page}.html", message="Not correct, the 6-digit number is something else.")


@app.route("/eighth/api")
def getData():
    currentTime = datetime.today().strftime('%Y-%m-%d %H:%M')
    messageContent = "The secret message: For the solution you will need to find those numbers first that will cause a special value to appear. For more look into the JS code."
    messageContent += f" Time sent: {currentTime}"
    message = {"message": f"{util.encryption_rail_fence(messageContent)}"}

    return jsonify(message)


@app.route("/ninth/api", methods=["POST"])
def handleInput():


    if "reached" not in session or session["reached"] < PAGEMAP.get("ninth").get("session"):
        return redirect("/")

    steps = ["first", "second", "third", "fourth", "fifth"]

    try:
        currentStep = request.json.get("step").strip()
        startingPosition = request.json.get("position").strip()
        adjustment = request.json.get("adjustment").strip()
        validateInputForNinthPage(currentStep, startingPosition, adjustment)
        changedPosition = calcNextPosition(currentStep, int(startingPosition), adjustment)
    except TypeError:
        return jsonify({"error": "Not correct type."})
    except ValueError:
        return jsonify({"error": "Not correct input."})
    except:
        return jsonify({"error": "incorrect data"})

    # First try or getting back to starting step
    if "positionsSum" not in session or currentStep == "first":
        session["positionsSum"] = 0

    session["positionsSum"] += changedPosition
    nextStep = steps[(steps.index(currentStep) + 1) % len(steps)]

    # After this was validated in validateInputForNinthPage, that correct step was sent
    session["nextStep"] = nextStep

    # Reaching last step
    if currentStep == "fifth":

        if util.verify_code(str(session["positionsSum"]), util.gethashes("ninth")):
            return jsonify({
                "currentPosition": changedPosition,
                "nextStep": nextStep,
                "solution": session["positionsSum"]})
        else:
            return jsonify({
                "currentPosition": changedPosition,
                "nextStep": nextStep,
                "solution": "Not correct, current position should be the starting position."})

    return jsonify({
        "currentPosition": changedPosition,
        "nextStep": nextStep})


def validateInputForNinthPage(currentStep, startingPosition, adjustment):
    if startingPosition is None or adjustment is None:
        raise ValueError
    try:
        int(startingPosition)
        int(adjustment)
    except:
        raise TypeError
    if currentStep not in ["first", "second", "third", "fourth", "fifth"]:
        raise ValueError
    if currentStep != "first" and "nextStep" not in session:
        raise ValueError
    if currentStep != "first" and currentStep != session["nextStep"]:
        raise ValueError



# adjustment handled as string for modifications for extracting actual number

def calcNextPosition(currentStep, startingPosition: int, adjustment: str):
    if currentStep == "first":
        numberExtracted = int(adjustment[-1])
        nextPos = startingPosition + (9 ** numberExtracted)
    elif currentStep == "second":
        numberExtracted = 0.5
        if int(adjustment) % 2 == 0:
            numberExtracted = 2
        nextPos = startingPosition * numberExtracted
    elif currentStep == "third":
        numberExtracted = len(adjustment) % 6
        nextPos = startingPosition / (6 - numberExtracted)
    elif currentStep == "fourth":
        numberExtracted = int(adjustment) % 3
        nextPos = startingPosition * 3 + 999999999 * numberExtracted
    elif currentStep == "fifth":
        numberExtracted = int(adjustment[-2:])
        nextPos = startingPosition - (numberExtracted + 21)
    else:
        raise ValueError
    return int(nextPos)




if __name__ == '__main__':
    app.run()

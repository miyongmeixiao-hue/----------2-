from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/next")
def next():
    return render_template("home.html")

@app.route("/cats")
def meet():
    return render_template("meet the cats.html")
@app.route("/luna")
def luna():
    return render_template("luna.html")

@app.route("/noir")
def noir():
    return render_template("noir.html")

@app.route("/momo")
def momo():
    return render_template("momo.html")

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/ok")
def ok():
    return render_template("ok.html")

@app.route("/company.html")
def company():
    return render_template("company.html")

@app.route("/event.html")
def event():
    return render_template("event.html")

@app.route("/next", methods=["GET", "POST"])
def speak():
    data=""

    if request.method == "POST":
        text = request.form["text"]
        hour = int(request.form["hour"])

        if len(text)<=5 and (hour >= 18 or hour <= 6):
             data="こんばんわ！"
        elif len(text)>=6:
            data="文字長すぎて理解出ないよ！！５文字以内でお願いします"
        else:
            data="にゃー（月の魔法がないため言葉がしゃべれないよ）"
        return render_template("home.html",data=data)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        people = request.form["people"]
    return render_template(
        "reservation-confirm.html",
        name=name,
        date=date,
        time=time,
        people=people
    )
            

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from game_logic import Game

app = Flask(__name__)
new_game = Game()


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.form:
        return redirect(url_for("guess"))
    return render_template("welcome.html")


@app.route("/guess", methods=["GET", "POST"])
def guess():

    if request.form:
        user_guess = int(request.form.get("guess"))
        new_game.guess(user_guess)
        result = new_game.check_win()

        if result == "win":
            new_game.reset()
            return render_template("result.html", result=result)
        elif result == "lose":
            new_game.reset()
            return render_template("result.html", result=result)
        else:
            return render_template("guess.html", game=new_game)
    return render_template("guess.html", game=new_game)


if __name__ == "__main__":
    app.run(debug=True)

from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Play madlibs game"""

    to_play = request.args.get("play-game")

    if to_play == "yes":
        return render_template("game.html")
    elif to_play == "no":
        return render_template("goodbye.html")
    else:
        return "We are not sure what %s means?!" % to_play

    print to_play

@app.route('/madlib')
def show_madlib():
    madlibs = ["madlib1.html", "madlib.html"]
    noun = request.args.get('noun')
    color = request.args.get('color')
    name = request.args.get('name')
    adjective = request.args.get('adj')
    pets = request.args.getlist('pets')
    madlib = choice(madlibs)
    
    return render_template( madlib,
                            noun=noun,
                            color=color,
                            person=name,
                            adjective=adjective,
                            pets=pets,
                            )


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

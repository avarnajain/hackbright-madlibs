"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """play game with user"""
    play = request.args.get("play")

    if play == 'dont_play':
        return render_template('goodbye.html')
    elif play == 'play':
        return render_template('game.html')


@app.route('/madlib')
def show_madlib():

    arg_dict = request.args
    arg_dict = request.args.items()
    adj_list = []

    for key in arg_dict:
        if 'adjective' in key:
            adj_list.append(arg_dict)

       
    # adjective_list = arg_dict.get('adjective')
    # [adj_tuple arg_dict.get('adjective')]

    return render_template('madlib.html', 
        arg_dict=arg_dict, adj_list = adj_list)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)


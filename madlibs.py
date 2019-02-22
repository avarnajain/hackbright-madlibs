"""A madlib game that compliments its users."""

from random import choice, choices

from flask import Flask, render_template, request, redirect, flash

from time import sleep

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

app.secret_key = 'testing-one'

@app.route('/')
def start_here():
    """Display homepage."""
    sleep(3)
    return redirect('http://localhost:5000/hello') 


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = choices(AWESOMENESS, k=3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """play game with user"""
    play = request.args.get("play")

    if play == 'dont_play':
        return render_template('goodbye.html')
    elif play == 'play':
        return render_template('game.html')


@app.route('/madlib', methods=["POST"])
def show_madlib():

    arg_dict = request.form
    adj_list = [value for key, value in arg_dict.items(multi=True) if key=='adjective']

    # create a list holding all possible html things
    # "choice" that, store as variable
    # pass variable into render_template

    MADLIB_TEMPLATES = ['madlib.html', 'madlib_2.html']

    template_to_use = choice(MADLIB_TEMPLATES)

    return render_template(template_to_use, 
        arg_dict=arg_dict, adj_list = adj_list)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)


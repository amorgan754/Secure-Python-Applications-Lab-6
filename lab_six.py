"""This project is to show the use of html code within python"""

#imports
from datetime import datetime
from flask import Flask
from flask import render_template


CURRENTDATE = datetime.now()

app = Flask(__name__)


#four routes to pull to the four different pages


#route to home page
@app.route('/')
def home():
    """This function is to pull in the home html code"""
    return render_template('home.html')


#route to current date time page, give link to world clock
@app.route('/datetime')
def date():
    """This function is to pull in the datetime html code"""
    datenow = CURRENTDATE.today()
    return render_template('datetime.html', datetime=datenow)


#route to a dad joke, give link to daily dad jokes
@app.route('/jokes')
def jokes():
    """This function is to pull in the jokes html code"""
    return render_template('jokes.html')


@app.route('/books')
def books():
    """This function is to pull the books html code"""
    return render_template('books.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

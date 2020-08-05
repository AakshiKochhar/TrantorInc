""" This program will open the quiz in an interactive window and have the user 
complete the quiz through the web application."""

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)  # Create instance of web application

questions = {"What is the fifth month of the year?":"May",
             "How many days in a leap year?":"366",
             "What is 2 + 5?":"7",
             "True/False - Eleven is a prime number.": "True",
             "True/False - 5449 is a prime number.": "True",
             "What is 1230 * 3084?": "3793320",
             "What is the 17th letter of the alphabet?": "Q",
             "True/False - The 29th letter of the Greek alphabet is Tau.": "False",
             "How many legs does a butterfly have?": "6",
             "What is 8 * 120?": "960",
             "True/False - The hashtag symbol is technically called an octothorpe.": "True",
             "True/False - Some cats are allergic to people.": "True",
             "What is 6869055 - 75594?": "679346",
             "True/False - Scotland's national symbol is the unicorn.": "True",
             "True/False - M&M stands for Mars & Milkyway.": "False",
             "True/False - The odds of getting a royal flush are exactly 1 in 649740.": "True",
             "What is (500 * (15 / (5 + 10)) - 3520) ** 2?": "9120400",
             "True/False - There are 15820024210 possible ten-card hands in gin rummy.": "False",
             "What is a baby puffin is called?": "Puffling",
             "What is 6 * 6549?": "39294",
             "True/False - The reason a bug is called a bug in CS is due to a bug being found in a computer.": "True",
             "What is 6869055 % 75594?": "65595"
             }



@app.route("/", methods=["POST", "GET"]) # Path will take user to the default home page of the game.
def login():
    return render_template("submitted.html", contents=questions)
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("submitted.html") # Combines template with given dictionary and 
                                                 # will return an HttpResponse object with that rendered text


@app.route("/submit") # Will load answers when user presses 'Submit Query' button.
def submit():
    return render_template("index.html", contents=questions)

if __name__ == "__main__":
    app.run(debug=True) 




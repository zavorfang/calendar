import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form['name']
        dob = request.form['date'].split('-')
        month= dob[1]
        day= dob[2]
        query = "INSERT INTO birthdays(name, month, day) VALUES(:name, :month, :day)"
        id = db.execute(query, name=name, month=month, day=day)
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        query = "SELECT * FROM birthdays"
        birthdays = db.execute(query)
        return render_template("index.html", users=birthdays)


if __name__ == "__main__":
    app.run(debug=True)
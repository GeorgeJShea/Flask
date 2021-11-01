
from flask import Flask, request, render_template, redirect, url_for
import math
app = Flask(__name__)
import cylinder #<--why?


@app.route("/sphere", methods = ["GET", "POST"])

def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form
       height = request.form.get("hgt")
       vol = cylinder.volume(int(radius), int(height))
       return "User entered: Radius "+ str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
   return render_template("cylinder.html")
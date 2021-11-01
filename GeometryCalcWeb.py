# SENG3110 Software Testing
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Orig Date: 9/22/2021
#
# imports
from flask import Flask, request, render_template, redirect, url_for
import math
import cylinder #<--why?

#flask plumbing
app = Flask(__name__)
#flask route for the index page
#uses html template for user selection
@app.route("/", methods = ["GET", "POST"])
def mainForm():
    try:
        if request.method == "POST":
          sphere = request.form.get("sphere")
          cylinder = request.form.get("cylinder")
          cone = request.form.get("cone")
          index = request.form.get("index")

          print("Selection was: ", sphere, cylinder, cone, index) #prints to command line for trouble shooting
          if sphere == "on":
             print("User selected sphere") #prints to command line for trouble shooting
             return redirect(url_for('sphereForm'))
          elif cylinder == "on":
             print("User selected cylinder") #prints to command line for trouble shooting
             return redirect(url_for('cylinderForm'))
          elif cone == "on":
              print("User selected cylinder")  # prints to command line for trouble shooting
              return redirect(url_for('coneForm'))
          else:
              print("else happened")
              return redirect(url_for("index.html"))
    except:
        print("ERROR")
        return redirect(url_for("index.html"))

    return render_template("index.html")

#flask route for the cylinder calculations page
@app.route("/cylinder", methods = ["GET", "POST"])

def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form
       height = request.form.get("hgt")
       vol = cylinder.volume(int(radius), int(height))
       return "User entered: Radius "+ str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
   return render_template("cylinder.html")

@app.route("/sphere", methods = ["GET", "POST"])
def sphereForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")

       vol = (4/3) * math.pi * radius^3
       return "User entered: Radius "+ str(radius) + " and Height: " + ". <p>The Volume is: " + str(vol)
   return render_template("sphere.html")

@app.route("/cone", methods = ["GET", "POST"])
def coneForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")

       #vol = (4/3) * math.pi * radius^3
       return "User entered: Radius "+ str(radius) + " and Height: " + ". <p>The Volume is: " + str(5)
   return render_template("cone.html")
#more code here for the rest of the calculators: sphere, cube, etc.
  
if __name__=='__main__':   #more flask plumbing so the environment starts correctly
   app.run(host='0.0.0.0')

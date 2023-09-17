# save this as app.py
from flask import Flask, request, render_template

# create an instance of the Flask class
app = Flask(__name__)

# define a function to check if a number is prime
def isPrime(n):
    # assume n is a positive integer
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# find the nearest prime number to n (not including n)
def nearestPrime(n):
    delta = 1
    # loop until a prime is found
    while True:
      if isPrime(n + delta):
        # return n + delta as the nearest prime
        return n + delta
      # check if n - delta is a prime and positive
      elif n - delta > 0 and isPrime(n - delta):
        return n - delta
      # increment the delta by 1
      else:
        delta += 1

# define a route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    # initialize the result and number variables
    result = None
    number = None
    closest = None
    delta = None

    # check if the request method is POST
    if request.method == "POST":
        # get the number input from the form
        number = request.form.get("number")

        # check if the number is valid
        try:
            number = int(number)
            if number < 1:
                raise ValueError

            # check if the number is prime and set the result accordingly
            if isPrime(number):
                result = "prime"
            else:
                result = "not prime"
                # find the nearest prime number
                closest = nearestPrime(number)
                delta = abs(number - closest)

        except ValueError:
            # handle invalid input and set the result accordingly
            result = "invalid"

    # render the index.html template with the result and number variables
    return render_template("index.html", result=result, number=number, closest=closest, delta=delta)

# run the app
# app.run()

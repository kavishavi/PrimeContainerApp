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

# get sum of digits
def getSum(n):  
    dsum = 0
    for digit in str(n): 
      dsum += int(digit)      
    return dsum

def getSumStr(n):   
    sumStr = ""
    i = 1
    for digit in str(n): 
      if (i==1):
        sumStr= sumStr + digit 
        i = i+1
      else:
        sumStr= sumStr + " + " + digit 
    return sumStr

def getSumDifStr(n):   
    sumDifStr = ""
    i = 1
    for digit in str(n): 
      if (i==1):
        sumDifStr= sumDifStr + digit 
        i = i + 1      
      elif (i % 2 == 0):
        sumDifStr= sumDifStr + " - " + digit 
        i = i + 1
      else:
        sumDifStr= sumDifStr + " + " + digit 
        i = i + 1
    return sumDifStr

# define a route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    # initialize the result and number variables
    result = None
    number = None
    closest = None
    delta = None
    ddsum = None
    strSum = None
    ddsumdif = None
    strSumDif = None

    # check if the request method is POST
    if request.method == "POST":
        # get the number input from the form
        number = request.form.get("number")

        # check if the number is valid
        try:
            number = int(number)
            if number < 1:
                raise ValueError
            
            # check if the number is even
            if number % 2 == 0:
               result = "even"
            elif number % 5 == 0:
               result = "divisible_by_5"
            # check if the number is prime and set the result accordingly
            elif number % 3 == 0:
               result = "divisible_by_3"
               ddsum = getSum(number)
               strSum = getSumStr(number)
            elif number % 11 == 0:
               result = "divisible_by_11"
               ddsumdif = 0
               strSumDif = getSumDifStr(number)
            elif isPrime(number):
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
    return render_template("index.html", result=result, number=number, closest=closest, delta=delta, ddsum=ddsum, strSum=strSum, ddsumdif=ddsumdif, strSumDif=strSumDif)

# run the app
# app.run()

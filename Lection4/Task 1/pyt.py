from flask import Flask, render_template, request

servak = Flask(__name__)

@servak.route('/')
def index():
    return render_template("index.html")

@servak.route("/sum")
def sum():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue + secondValue)

@servak.route("/min")
def min():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue - secondValue)

@servak.route("/root")
def root():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue**(1/secondValue))

@servak.route("/power")
def power():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue**secondValue)

@servak.route("/divide")
def divide():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue / secondValue)

@servak.route("/multip")
def multip():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    return str(firstValue * secondValue)

if __name__ == "__main__":
    servak.run(debug=True)
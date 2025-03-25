#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route("/count/<int:num>")
def count(num):
    numbers = "\n".join(str(i) for i in range(num)) + "\n" # Fix the off-by-one error
    return numbers  # Ensure plain text output

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation. Use +, -, *, div, or %."

    return str(result)  # Return just the number as a string
if __name__ == '__main__':
    app.run(port=5555, debug=True)

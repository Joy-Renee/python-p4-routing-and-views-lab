#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<name>')
def name(name):
    return f'<h1>{name} </h1>'

@app.route('/print/hello')
def hello():
    print('hello')
    return 'hello'

# @app.route('/count/<int:number>')
# def number(number):
#     return f'{range(number)}'

@app.route('/count/<int:parameter>')
def count(parameter):
    count_string = "\n".join(str(i) for i in range(parameter)) + '\n'
    return count_string

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def add(num1,operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        if num2 == 0:
            return 'Division by 0 is not allowed'
        result = num1 % num2
    elif operation == 'div': 
        result = num1 / num2
    else:
        "Invalid option"

    return str(result)
     


if __name__ == '__main__':
    app.run(port=5555, debug=True)

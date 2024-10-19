from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])

def calculate():
    try:
        print("Function calculate called")
        results = []

        multiplicator = float(request.form['multiplicator'])
        print(f"Multiplicator: {multiplicator}") # debug
        values = int(request.form['values'])
        print(f"values: {values}") # debug

        # operação
        number = 0
        while number <= values:
            result = multiplicator * number
            results.append(f"{multiplicator} x {number} = {result}")
            number += 1
        print(f"results: {results}")
        print(results)
    except ValueError as error:
        results = "ERROR, enter only numbers!"
        print(f"Error: {error}")
    
    if results is None:
        print("results is None, setting a default message")  # Log de depuração
        results = "No calculation performed."

    return render_template('index.html', results=results)
    
if __name__ == '__main__':
    app.run(debug=True)
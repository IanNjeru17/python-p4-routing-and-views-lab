from flask import Flask

app = Flask(__name__)

# Root route: Displays a message in h1
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a parameter passed in the URL
@app.route('/print/<string:text>')
def print_text(text):
    print(text)  # Display the text in the console
    return text  # Display the text in the browser

# Route to count through a range of numbers and display on separate lines
@app.route('/count/<int:number>')
def count(number):
    return '\n'.join([str(i) for i in range(number)]) + '\n'  # Output with newline at the end

# Route to perform math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation or division by zero.', 400
    
    return str(result)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

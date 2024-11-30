from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template for the Calculator
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Calculator</title>
</head>
<body>
    <h1>Web Calculator</h1>
    <form method="post" action="/">
        <label for="a">Enter first number:</label>
        <input type="number" step="any" name="a" required><br><br>
        <label for="b">Enter second number:</label>
        <input type="number" step="any" name="b" required><br><br>
        <label for="operation">Choose an operation:</label>
        <select name="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
    {% if error is not none %}
    <h2 style="color:red;">Error: {{ error }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            operation = request.form.get("operation")
            
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    error = "Division by zero is not allowed."
                else:
                    result = a / b
            else:
                error = "Invalid operation selected."
        except ValueError:
            error = "Invalid input! Please enter valid numbers."
    
    return render_template_string(HTML_TEMPLATE, result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

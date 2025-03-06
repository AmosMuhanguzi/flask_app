from flask import Flask, request

app = Flask(__name__)

balance = 0  # Global balance (not persistent)

def generate_html(message=""):
    """Generates an HTML string with the current balance and message."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Banking App</title>
    </head>
    <body>
        <h1>Banking App</h1>
        <p>Current Balance: ${balance}</p>

        <form method="POST" action="/deposit">
            <label for="depositAmount">Deposit Amount:</label>
            <input type="number" id="depositAmount" name="amount" required>
            <button type="submit">Deposit</button>
        </form>

        <form method="POST" action="/withdraw">
            <label for="withdrawAmount">Withdraw Amount:</label>
            <input type="number" id="withdrawAmount" name="amount" required>
            <button type="submit">Withdraw</button>
        </form>

        <p style="color: red;">{message}</p>

    </body>
    </html>
    """
    return html_content

@app.route('/', methods=['GET'])
def index():
    print("Index route accessed") # Debugging line
    return generate_html()

@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    try:
        amount = float(request.form['amount'])
        if amount > 1000:
            balance += amount
            return generate_html(f"Deposited ${amount}.")
        else:
            return generate_html("Amount must be greater than 1000.")
    except ValueError:
        return generate_html("Invalid amount.")

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    try:
        amount = float(request.form['amount'])
        if amount > 500:
            if balance >= amount:
                balance -= amount
                return generate_html(f"Withdrew ${amount}.")
            else:
                return generate_html("Insufficient balance.")
        else:
            return generate_html("Amount must be greater than 500.")
    except ValueError:
        return generate_html("Invalid amount.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
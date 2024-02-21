from flask import Flask, jsonify, request, send_file, render_template, make_response, redirect, url_for
import bot

app = Flask(__name__)

# Define a route for '/bot' that handles both POST and GET requests
@app.route('/bot', methods=['POST', 'GET'])
def hello_world():
    # Check if the request method is POST
    if request.method == 'POST':
        # Access the 'nm' value from the form data submitted with the POST request
        txt = request.form['nm']

        # Call a function from the 'bot' module (assuming it's a custom module in your project)
        bot_said = bot.ApiChat(txt)

        # Render the 'bot.html' template and pass the 'bot_said' value to it
        return render_template('bot.html', name=bot_said)

    # If the request method is GET, render the 'bot.html' template without processing form data
    else:
        return render_template('bot.html')

# Define a route for the root URL ('/')
@app.route('/')
def Index():
    # Render the 'index.html' template
    return render_template('index.html')

# Define a route for '/home'
@app.route('/home')
def Home():
    # Render the 'home.html' template
    return render_template('home.html')

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

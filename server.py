from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract form data
        username = data.get('username')
        email = data.get('email')
        reason = data.get('reason')
        other_reason = data.get('other_reason', None)
        
        # Here, you would typically save the data to a database or perform any necessary actions
        # For now, we're just printing the received data
        print(f"New Signup:\nUsername: {username}\nEmail: {email}\nReason: {reason}\nOther Reason: {other_reason}")
        
        # You can add any custom logic for handling different reasons, validating inputs, etc.
        
        # Respond with a success message
        return jsonify({
            'success': True,
            'message': 'Signup successful!'
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your request.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

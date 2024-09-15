from flask import Flask, request, jsonify
import util  # Ensure util has the functions get_locations_name and get_estimated_price

app = Flask(__name__)

# Call the function to load saved artifacts when the app starts
util.load_saved_artifacts()

# Route for getting location names
@app.route('/get_locations_name', methods=['GET'])
def get_locations_name():
    # Fetch the locations from util
    locations = util.get_locations_name()
    
    if locations is None:
        return jsonify({"error": "Locations not loaded"}), 500
    
    response = jsonify({
        "locations": locations
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response  # Returning the actual JSON response

# Route for predicting home price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Ensure that all required form fields are present
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Get the estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    except Exception as e:
        # Return error in case of issues
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)

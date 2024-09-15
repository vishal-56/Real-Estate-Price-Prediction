Real Estate Price Prediction - Bengaluru
This project predicts real estate prices in Bengaluru based on key factors like square footage, number of bedrooms (BHK), bathrooms, and location. The model uses machine learning to estimate property prices, and the web application is built using Flask for the backend and a simple frontend for user interaction.

Dataset
Source: The dataset (bengaluru_house_prices.csv) contains property prices in Bengaluru.
Features: location, total_sqft, bath, bhk.
Project Structure
bash
Copy code
├── client
│   ├── app.css
│   ├── app.html
│   └── app.js
├── server
│   ├── server.py
│   ├── util.py
│   └── artifacts
│       ├── real_estate.pickle
│       └── Columns.json
├── bengaluru_house_prices.csv
├── README.md
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/vishal-56/Real-Estate-Price-Prediction.git
cd Real-Estate-Price-Prediction
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask server:

bash
Copy code
python server/server.py
Open client/app.html in a browser.

Usage
Get Location Names: Use the /get_locations_name endpoint to fetch dynamic locations for the dropdown.
Predict Home Price: Submit total square feet, BHK, bathroom count, and location to /predict_home_price to get an estimated price.
API Endpoints
/get_locations_name (GET): Returns the list of available locations.
/predict_home_price (POST): Takes user input (location, square feet, BHK, bath) and returns the predicted price.
Technologies Used
Python: Backend logic and machine learning.
Flask: Web framework.
Pandas, Numpy: Data preprocessing.
Jupyter Notebook: Model training and experimentation.
HTML, CSS, JavaScript (jQuery): Frontend development.

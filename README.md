# Real Estate Price Prediction - Bengaluru

This project predicts real estate prices in Bengaluru based on key factors like square footage, number of bedrooms (BHK), bathrooms, and location. The model uses machine learning to estimate property prices, and the web application is built using Flask for the backend and a simple frontend for user interaction.

## Dataset
- **Source**: The dataset (`bengaluru_house_prices.csv`) contains property prices in Bengaluru.
- **Features**: `location`, `total_sqft`, `bath`, `bhk`.

## Project Structure
```bash
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
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vishal-56/Real-Estate-Price-Prediction.git
   cd Real-Estate-Price-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   python server/server.py
   ```

4. Open `client/app.html` in a browser.

## Usage
1. **Get Location Names**: Use the `/get_locations_name` endpoint to fetch dynamic locations for the dropdown.
2. **Predict Home Price**: Submit total square feet, BHK, bathroom count, and location to `/predict_home_price` to get an estimated price.

## API Endpoints

1. **`/get_locations_name`** (GET): Returns the list of available locations.
2. **`/predict_home_price`** (POST): Takes user input (location, square feet, BHK, bath) and returns the predicted price.

## Technologies Used
- **Python**: Backend logic and machine learning.
- **Flask**: Web framework.
- **Pandas, Numpy**: Data preprocessing.
- **Jupyter Notebook**: Model training and experimentation.
- **HTML, CSS, JavaScript (jQuery)**: Frontend development.

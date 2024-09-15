import json
import pickle
import numpy as np
import pandas as pd  # Required for DataFrame manipulation
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Initialize an array of zeros with the same length as the number of columns
        x = np.zeros(len(__data_columns))
        
        # Set the corresponding values for sqft, bath, and bhk
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        # Check if the location exists in the columns (i.e., one-hot encoded)
        if location.lower() in __locations:
            loc_index = __data_columns.index(location.lower())  # Get the location index
            x[loc_index] = 1  # Set the value for the location to 1 (one-hot encoding)
        
        # Make a prediction using the trained model
        return round(__model.predict([x])[0], 2)  # Predict and round the output to 2 decimal places
    except Exception as e:
        return f"Error: {str(e)}"

def get_locations_name():
    return __locations

def load_saved_artifacts():
    print("loading saved artifact.....start")
    global __data_columns
    global __locations
    global __model

    # Load the column names from the correct path
    with open('./server/artifacts/Columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Assuming location columns start at index 3

    # Load the trained model from the correct path
    with open('./server/artifacts/real_estate.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts .......done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_locations_name())
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))

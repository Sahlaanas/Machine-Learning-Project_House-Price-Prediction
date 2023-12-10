import streamlit as st
import pickle 
import json

with open('/Users/mac/Desktop/bnglr_hs_prdcn_project/model/columns.json', 'r') as json_file:
    data = json.load(json_file)
    columns = data['data_columns']

model = pickle.load(open('/Users/mac/Desktop/bnglr_hs_prdcn_project/model/bglr_house_price_model.pickle','rb'))


import streamlit as st
import numpy as np

# Assuming `columns` and `model` are defined elsewhere in your Streamlit app
# If not, you need to load them or define them in this file.
house_image_url = 'https://blog.hubspot.com/hubfs/Sales_Blog/real-estate-business-compressor.jpg'
st.image(house_image_url, use_column_width=True)
st.title('House Price Prediction')

def formInfo():
    # Get input values from the user
    location_options = columns  # Assuming `columns` contains location options
    location = st.selectbox('Location', location_options)
    location = location.lower()
    bhk = st.number_input('BHK', min_value=1, max_value=10, step=1)
    area = st.number_input('Area (sq. ft.)', min_value=1, step=1)
    bath = st.number_input('Number of Bathrooms', min_value=1, step=1)

    # Assuming `columns` is defined elsewhere in your Streamlit app
    loc_index = columns.index(location) if location in columns else -1

    # Create the input vector for prediction
    x = np.zeros(len(columns))
    x[0] = area
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Assuming `model` is defined elsewhere in your Streamlit app
    y_pred = model.predict([x])[0]

    # Display the prediction
    st.write('Predicted Price:', np.round(y_pred) * 10000)

# Run the Streamlit app
if __name__ == '__main__':
    formInfo()

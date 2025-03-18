import streamlit as st
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

# Load the model
loaded_model = keras.models.load_model('model.h5')

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((150, 150))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Streamlit app
st.title("Dog-Cat Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    processed_image = preprocess_image(image)
 
    predictions = loaded_model.predict(processed_image)
    st.write(predictions)

   
    if predictions[0] > 0.5:
        st.write("It's a Dog!")
    else:
        st.write("It's a Cat!")
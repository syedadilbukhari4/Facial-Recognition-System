import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import io
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😊",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .prediction-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('fer_model.h5')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Preprocess image
def preprocess_image(image):
    try:
        # Convert to grayscale
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # Resize to 48x48
        image = cv2.resize(image, (48, 48))
        
        # Normalize
        image = image.astype('float32') / 255.0
        
        # Reshape for model input
        image = np.expand_dims(image, axis=[0, -1])
        return image
    except Exception as e:
        st.error(f"Error preprocessing image: {str(e)}")
        return None

# Emotion labels
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# App title and description
st.title("Facial Emotion Recognition By Syed Adil Bukhari")
st.markdown("Upload an image containing a face to predict the emotion.")

# Load model
model = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    try:
        # Read and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Convert PIL Image to numpy array
        image_np = np.array(image)
        
        # Preprocess image
        processed_image = preprocess_image(image_np)
        
        if processed_image is not None and model is not None:
            # Make prediction
            predictions = model.predict(processed_image)[0]
            
            # Get the predicted emotion
            predicted_emotion = emotions[np.argmax(predictions)]
            
            # Display prediction
            st.markdown("### Prediction")
            st.markdown(f"""
                <div class="prediction-box">
                    <h3>Predicted Emotion: {predicted_emotion.capitalize()}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            # Display probabilities as a bar chart
            st.markdown("### Emotion Probabilities")
            chart_data = pd.DataFrame({
                'Emotion': emotions,
                'Probability': predictions
            })
            st.bar_chart(chart_data.set_index('Emotion'))
            
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        st.info("Please make sure you've uploaded a valid image file containing a face.") 
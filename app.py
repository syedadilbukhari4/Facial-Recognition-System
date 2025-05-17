import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import io

# Set page config
st.set_page_config(
    page_title="Emotion Detection App By Adil Bukhari",
    page_icon="😊",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("fer_model.h5")

# Initialize model
model = load_model()
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def preprocess_image(image):
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Resize to 48x48
    image = cv2.resize(image, (48, 48))
    # Normalize
    image = image.astype("float32") / 255.0
    # Add batch and channel dimensions
    image = np.expand_dims(image, axis=(0, -1))
    return image

# App title and description
st.title("Emotion Detection App")
st.write("Upload an image of a face to detect the emotion!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert PIL Image to numpy array
    image_np = np.array(image)
    
    # Process image and make prediction
    processed_image = preprocess_image(image_np)
    predictions = model.predict(processed_image)[0]
    
    # Get the predicted emotion
    predicted_emotion = emotions[np.argmax(predictions)]
    
    # Display results
    st.subheader("Results")
    st.write(f"Predicted Emotion: {predicted_emotion}")
    
    # Create a bar chart of probabilities
    st.subheader("Emotion Probabilities")
    prob_dict = {emotions[i]: float(predictions[i]) for i in range(len(emotions))}
    st.bar_chart(prob_dict) 
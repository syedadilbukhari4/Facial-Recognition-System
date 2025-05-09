# Facial Emotion Recognition Web App

This is a Streamlit web application that uses a pre-trained Keras model to predict facial emotions from uploaded images.

## Features

- Upload and process facial images
- Automatic image preprocessing (resize to 48x48, grayscale conversion)
- Real-time emotion prediction
- Display of prediction probabilities
- Clean and modern UI
- Error handling for invalid inputs

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure the `fer_model.h5` file is in the project root directory.

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. Open the web app in your browser (default: http://localhost:8501)
2. Upload an image containing a face
3. The app will automatically process the image and display:
   - The uploaded image
   - The predicted emotion
   - A bar chart showing probabilities for all emotions

## Supported Image Formats

- JPG/JPEG
- PNG

## Note

The model expects 48x48 grayscale images. The app automatically handles the preprocessing of uploaded images to match these requirements. 
# Facial Emotion Recognition Streamlit App

This is a web application that uses a pre-trained Keras model to predict facial emotions from uploaded images. The app is built using **Streamlit** for a simple and interactive user interface.

## 🚀 Features

- Upload and analyze facial images
- Automatic preprocessing (resize to 48x48, grayscale conversion)
- Real-time emotion prediction
- Bar chart visualization of prediction probabilities
- Simple, modern UI

---

## 📦 Project Structure

```
facial-emotion-app/
├── app.py              # Streamlit app
├── fer_model.h5        # Pretrained Keras model (not included in repo)
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## 🔧 Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/facial-emotion-app.git
cd facial-emotion-app
```

### 2. Add Model
Place your trained `fer_model.h5` file in the root directory.

### 3. Install Dependencies
It is recommended to use a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501` by default.

---

## 📝 Notes
- Make sure your `fer_model.h5` is compatible with TensorFlow 2.x.
- No FastAPI or separate frontend is needed—everything runs in Streamlit!
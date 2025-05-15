# Facial Emotion Recognition Web App (Vercel Deployment)

This is a serverless web application that predicts facial emotions from uploaded images using a pre-trained Keras model. The backend is built with **FastAPI** and the frontend can be plain HTML/JS or a modern framework like **Next.js**. Deployed seamlessly on **Vercel**.

---

## ✨ Features

- Upload face image via web interface
- Serverless FastAPI backend for emotion prediction
- Uses a CNN model trained on FER-2013 dataset
- Emotion probabilities and predicted label returned
- Easy to deploy via Vercel (no Streamlit)

---

## 🧠 Supported Emotions

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

---

## 🗂 Project Structure

emotion-recognition-vercel/
├── api/
│ └── predict.py # FastAPI function (Vercel serverless)
├── fer_model.h5 # Pre-trained Keras model
├── frontend/ # Optional: simple HTML frontend
│ └── index.html
├── requirements.txt # Python dependencies
├── vercel.json # Vercel config
└── README.md
## 🚀 Getting Started (Local Testing)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI app locally:

bash
Copy
Edit
uvicorn api.predict:app --reload
Open http://127.0.0.1:8000/docs to test the API using Swagger UI.

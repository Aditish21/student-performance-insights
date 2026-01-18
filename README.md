# 🎓 Student Performance Prediction System (End-to-End ML Project)

An industry-style, end-to-end Machine Learning application** that predicts whether a student will **Pass or Fail** based on academic and behavioral features.
The project covers the **complete ML lifecycle** — from data processing and model training to **API deployment, frontend integration, Dockerization, and live deployment**.

> 🚀 This project is built to be **resume-ready, interview-ready, and production-oriented**.

## 📌 Project Overview

Educational institutions often need early insights into student performance to provide timely support. This project uses **Logistic Regression** to predict student outcomes and exposes the model through a **FastAPI backend**, with a **Streamlit-based frontend** for real-time interaction.

The system predicts:

* **Pass / Fail status**
* **Probability of passing** (confidence-based decision making)

## 🧠 Key Concepts Implemented

* Supervised Machine Learning (Classification)
* Logistic Regression with Sigmoid Function
* Probability-based prediction (`predict_proba`)
* Threshold tuning for real-world decision making
* Model evaluation using:

  * Accuracy
  * Confusion Matrix
  * Precision, Recall, F1-score
* REST API development using FastAPI
* Interactive frontend using Streamlit
* Docker containerization
* Production-style project structure

---

## 🗂️ Project Structure

```
student-performance-ml/
│
├── src/
│   ├── logistic_regression.py   # Model training & evaluation
│   ├── api.py                   # FastAPI backend
│   └── model.pkl                # Trained ML model
│
├── streamlit_app.py              # Streamlit frontend
├── requirements.txt              # Project dependencies                 
├── README.md                     # Project documentation
└── data/
    └── student_data.csv          # Dataset
```

---

## 📊 Dataset Description

The dataset contains academic and behavioral features of students:

| Feature        | Description                  |
| -------------- | ---------------------------- |
| Study_Hours    | Average daily study hours    |
| Attendance     | Attendance percentage        |
| Previous_Score | Score in previous assessment |
| Final_Score    | Final exam score             |

### Target Variable

* **Pass_Fail**

  * `1` → Pass (Final_Score ≥ 60)
  * `0` → Fail (Final_Score < 60)

---

## 🤖 Machine Learning Model

### Model Used

* **Logistic Regression**

### Why Logistic Regression?

* Suitable for binary classification
* Outputs probability instead of raw class
* Interpretable coefficients
* Widely used in industry for decision systems

### Features Used

* Study_Hours
* Attendance
* Previous_Score

---

## 📈 Model Evaluation

The model is evaluated using industry-standard metrics:

* Accuracy
* Confusion Matrix
* Precision, Recall, F1-score

Additionally, **custom probability thresholds** are applied to simulate real-world decision control instead of relying only on the default 0.5 threshold.

---

## 🌐 FastAPI Backend

The trained model is deployed as a **REST API** using FastAPI.

### Available Endpoints

* `GET /` → Health check
* `POST /predict` → Predict student performance

### Example Request

```json
{
  "study_hours": 6,
  "attendance": 85,
  "previous_score": 70
}
```

### Example Response

```json
{
  "prediction": "Pass",
  "probability": 0.87
}
```

FastAPI also provides an **auto-generated Swagger UI** at:

```
http://localhost:8000/docs
```

---

## 🖥️ Streamlit Frontend

A clean and interactive **Streamlit web application** allows users to:

* Enter student details
* Send requests to the FastAPI backend
* View predictions and probabilities in real time

The frontend communicates with the backend via HTTP requests, following a **real production architecture**.

---

## 🚀 Deployment

The application is deployed as a **live web service** using a cloud platform .

✔ Backend (FastAPI on Render):
https://student-performance-insights.onrender.com/
✔Frontend (Streamlit Community Cloud):
https://student-performance-insights-wwkdj8lq6nappkt9ksuhj2y.streamlit.app/
✔ End-to-end ML system
✔ Production-style deployment

---

## 🧪 How to Run Locally (Without Docker)

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the model

```bash
python src/logistic_regression.py
```

### 3️⃣ Start FastAPI

```bash
uvicorn src.api:app --reload
```

### 4️⃣ Start Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 💼 Resume-Ready Highlights

* Built an **end-to-end ML application** from scratch
* Implemented **probability-based decision making**
* Deployed ML model using **FastAPI**
* Designed interactive UI using **Streamlit**
* Followed **industry-level project structure**

---

## 🎯 Future Enhancements

* Feature scaling & pipeline integration
* ROC-AUC analysis
* Model comparison (Decision Tree, Random Forest)
* Authentication for API
* CI/CD pipeline

---

## 👩‍💻 Author

**Aditi Sharma**
Artificial Intelligence & Data Science Student

> Passionate about Machine Learning, Deployment, and Building Real-World AI Systems.

---

⭐ If you find this project useful, feel free to star the repository and share feedback.

# **Name:** SATVIK SHARMA | **Club:** DCoders Squad - Machine Learning | **Date:** 21 March 2026

**Connect with me:**
* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]([https://www.linkedin.com/in/your-profile-url](https://www.linkedin.com/in/satvik-sharma-577835372))
* [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Satvik2Sharma)
* [Email Me](mailto:satviksharma1706@gmail.com)
# 💻 Laptop Price Prediction Web App
**DCoders Squad - Machine Learning Team | Task 2/5 Submission**

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Model-XGBoost-orange?style=for-the-badge)
![Flask](https://img.shields.io/badge/Backend-Flask-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap_5-purple?style=for-the-badge&logo=bootstrap)
![Render](https://img.shields.io/badge/Deployed_on-Render-black?style=for-the-badge&logo=render)

## 📌 Project Overview
This repository contains the final submission for **Task 5: Model Deployment with Frontend & Backend**. It transforms a trained Machine Learning regression model into a fully functional, live web application that predicts laptop prices based on hardware specifications.

## 👉 **[Click Here to view the Live Deployed Application]([https://satvik-sharma-laptop-price-predictor.onrender.com])** ---

## ✅ Task 2/5 Requirements Checklist
This project successfully fulfills all mandatory requirements outlined by the ML Leaders:

- [x] **Model Integration:** Integrated a highly tuned XGBoost regression model (saved via Pickle) to process real-world inputs.
- [x] **Backend Development:** Developed a RESTful API using **Flask** to handle frontend requests, process one-hot encoded arrays, and return predictions.
- [x] **Frontend Development:** Built a responsive, user-friendly interface using HTML, CSS, and Bootstrap 5 where users can input laptop specs via dropdowns and numerical fields.
- [x] **Deployment:** Successfully deployed both the frontend and backend on **Render** (using Gunicorn) for public web access.
- [x] **Jupyter Notebook:** Included `train.ipynb` detailing data preprocessing, model training, cross-validation, and evaluation.

---

## 📂 Repository Structure
```text
laptop-price-predictor/
│
├── app.py                 # The Flask Backend API
├── train.ipynb            # Jupyter Notebook with EDA, Model Training, & Evaluation
├── laptop_data.csv        # The cleaned dataset used for training
├── model.pkl              # Serialized XGBoost Regressor model
├── columns.pkl            # Serialized list of feature columns for backend mapping
├── requirements.txt       # Dependencies for cloud deployment
└── templates/
    └── index.html         # The Frontend HTML/Bootstrap interface

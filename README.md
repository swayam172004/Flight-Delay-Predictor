🚀 Flight Delay Predictor

  Machine Learning–powered web application that predicts:

✈️ Flight Delay Status (Delayed / On-Time)

🕒 Estimated Delay Duration (in minutes)

  Built using XGBoost, Scikit-Learn, and Streamlit for real-time predictions.

🌐 Live Demo

  👉[Click](https://flight-delay-predictor-tckelcwe8us5hkvdqjg4y7.streamlit.app/)

📌 Problem Statement

  Flight delays cause significant operational and financial challenges in aviation.
  This project uses machine learning to:
  
  Predict whether a flight will be delayed
  
  Estimate delay duration if delayed
  
  Provide real-time predictions via a clean web interface

🧠 Machine Learning Models
1️⃣ Classification Model

  Algorithm: XGBoost Classifier

  Output: Delay (Yes / No)

2️⃣ Regression Model

  Algorithm: XGBoost Regressor
  
  Output: Delay time in minutes

🛠 Tech Stack
Category               	Technology

Language	              Python 3.10
ML Models	              XGBoost
ML Framework	          Scikit-Learn
Web Framework	          Streamlit
Data Handling	          Pandas, NumPy
Model Storage	          Joblib

📂 Project Structure
Flight-Delay-Predictor/
│
├── app/
│   ├── main.py
│   ├── utils.py
│
├── models/
│   ├── classification_model.joblib
│   └── regression_model.joblib
│
├── requirements.txt
├── README.md
└── LICENSE

⚙️ Installation (Run Locally)

git clone https://github.com/swayam172004/Flight-Delay-Predictor.git
cd Flight-Delay-Predictor
pip install -r requirements.txt
streamlit run app/main.py

📊 Features

✔ Real-time delay prediction
✔ Clean & interactive UI
✔ Classification + Regression
✔ Deployment-ready architecture
✔ Error handling for production

🔐 Deployment

Deployed using : Streamlit Cloud


📈 Future Improvements

*Add weather data integration

*Improve model accuracy

*Add historical analytics dashboard

*CI/CD pipeline integration

👨‍💻 Author

Swayam Singh Sikarwar

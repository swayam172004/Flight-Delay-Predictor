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

⚠️ Engineering Challenges Faced
1️⃣ Large Dataset Handling (7–8 Lakh Rows, 32 Columns)
One of the major challenges during development was handling a high-volume dataset (~700,000–800,000 rows with 32 features).
Due to hardware limitations (local machine memory constraints), direct in-memory processing using Pandas caused performance bottlenecks and instability.
🔍 Problem
High RAM consumption during preprocessing
Slower DataFrame operations
System lag and memory overflow issues
Difficulty in model training using raw CSV files
🛠️ Solution Implemented
Instead of reducing the dataset size (which could compromise model integrity), I implemented a structured data pipeline:
Split and structured raw data efficiently
Transferred data into a SQL database
Performed preprocessing and cleaning directly at the database level
Built a pipeline that fetched processed data from SQL
Trained the machine learning model directly using database-connected architecture
💡 Why This Approach Matters
Reduced memory load on local system
Improved data handling efficiency
Simulated production-level architecture
Demonstrated database-integrated ML workflow
Built a scalable pipeline instead of a notebook-only solution
This challenge strengthened my understanding of:
Data engineering fundamentals
SQL integration with ML workflows
Memory optimization strategies
Designing scalable machine learning systems

📈 Future Improvements

*Add weather data integration

*Improve model accuracy

*Add historical analytics dashboard

*CI/CD pipeline integration

👨‍💻 Author

Swayam Singh Sikarwar


# 🏏 IPL Winner Predictor

A machine learning-powered web app that predicts the outcome of Indian Premier League (IPL) matches based on match context. Built using **Streamlit**, trained with **Random Forest**, and deployed on **Render**.

🔗 **Live App**: [https://ipl-winner-predictor-uhtf.onrender.com](https://ipl-winner-predictor-uhtf.onrender.com)

---

## 📌 Project Overview

This project leverages historical IPL data to predict the winner of a match in real-time. Given the current match situation—like runs left, balls remaining, and required run rate—the model predicts which team is more likely to win.

---

## 📁 Dataset

Two datasets were used:

### 1. `matches.csv`
- Metadata of 756 IPL matches
- Key columns: `id`, `season`, `team1`, `team2`, `toss_winner`, `winner`, `venue`, etc.

### 2. `deliveries.csv`
- Ball-by-ball data of 179,078 deliveries
- Key columns: `match_id`, `inning`, `batting_team`, `bowling_team`, `total_runs`, etc.

---

## 🧹 Data Preprocessing

1. **Total Score Calculation**:  
   Calculated total score for 1st innings and determined the target score as `total_runs + 1`.

2. **Merged Datasets**:  
   Created `match_df` by merging `matches` and `total_score_df` on `id` and `match_id`.

3. **Feature Engineering**:  
   Merged `match_df` with `deliveries` for 2nd innings only to create `delivery_df`, and engineered:
   - `current_score`: Cumulative sum of `total_runs`
   - `runs_left`: Target - current_score
   - `balls_left`: Derived from over and ball info
   - `current_run_rate` (CRR)
   - `required_run_rate` (RRR)

4. **Encoding**:  
   Applied one-hot encoding to categorical features: `batting_team`, `bowling_team`, and `city`.

---

## 🤖 Model Training

### Logistic Regression
- Accuracy: 80%
- Balanced performance

### Random Forest Classifier
- Accuracy: **100%** on test set
- Chosen as final model

### Saved Artifacts
- `RFmodel.pkl`: Trained Random Forest model
- `city.pkl`, `teams.pkl`: Encoded label mappings

---

## 💻 Web Application

Built using **Streamlit**, the app lets users select:
- Batting and bowling teams
- Match city
- Current score, overs, and wickets

The app displays the winning probability for each team.

### ▶️ Run Locally

```bash
git clone https://github.com/your-username/ipl-winner-predictor.git
cd ipl-winner-predictor
pip install -r requirements.txt
streamlit run app.py
```

### 🌐 Deployed App
Access the app live:  
🔗 [https://ipl-winner-predictor-uhtf.onrender.com](https://ipl-winner-predictor-uhtf.onrender.com)

---

## 📦 Project Structure

```
├── app.py                      # Streamlit application
├── matches.csv                 # Match metadata
├── deliveries.csv              # Ball-by-ball data
├── IPL Winner Predictor.ipynb  # EDA & Model building
├── RFmodel.pkl                 # Trained model file
├── city.pkl, teams.pkl         # Encoded data for inference
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

---

## 🚀 Future Work

- Integrate live match data via web scraping or API
- Use recent IPL seasons to improve model accuracy
- Enhance UI with real-time visualizations and win-probability graphs

---

## 🙏 Acknowledgements

- Dataset Source: [Kaggle IPL Dataset]([https://www.kaggle.com/datasets](https://www.kaggle.com/datasets/haroon669/ipl-matches-and-deliveries-dataset))
- Libraries: Pandas, Scikit-learn, Streamlit, Render

---

## 📬 Contact

Feel free to reach out for collaboration or questions.

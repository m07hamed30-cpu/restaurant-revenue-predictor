# 🍽️ Restaurant Revenue Predictor

A Machine Learning web app that estimates a restaurant's **expected monthly revenue** before you invest in it, based on historical data from existing restaurants.

![R² Score](https://img.shields.io/badge/R²-0.938-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Description

Opening a new restaurant is a costly investment. Before committing capital, an owner needs a data-driven estimate of expected revenue rather than guesswork.

This project trains a regression model on historical restaurant data (customer traffic, menu pricing, marketing spend, cuisine type, seating capacity, promotions, and reviews) and uses it to predict the **expected monthly revenue** of a new restaurant, given its characteristics — served through an interactive Streamlit web app.

## 🎯 Problem It Solves

- Restaurant investors and owners currently rely on intuition or rough industry benchmarks to estimate revenue potential.
- This tool provides an instant, data-backed revenue estimate from a handful of restaurant characteristics, supporting better go/no-go investment decisions.

## ✨ Features

- Clean, interactive Streamlit UI for entering restaurant characteristics
- Instant monthly revenue prediction
- Model trained and validated on 1,192 historical restaurant records
- Full transparency: notebook with EDA, cleaning, feature engineering, model comparison, and tuning
- Comprehensive study-guide documentation (`docs/PROJECT_EXPLANATION.md`)

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Data handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn, xgboost |
| Model persistence | joblib |
| Web app | Streamlit |

## 📁 Project Structure

```
restaurant-revenue-predictor/
├── data/
│   └── Restaurant_Revenue_Dataset.csv
├── notebooks/
│   └── AI_Restaurant_Revenue_Prediction.ipynb
├── model/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
├── docs/
│   └── PROJECT_EXPLANATION.md
├── screenshots/
│   └── (place app screenshots here)
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── PROJECT_STRUCTURE.md
├── PRESENTATION_NOTES.md
├── FAQ.md
└── INTERVIEW_QA.md
```

See [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) for a description of every file and folder.

## 📊 Dataset

`data/Restaurant_Revenue_Dataset.csv` — 1,208 rows (1,192 after cleaning), 9 columns:

| Column | Description |
|---|---|
| `Number_of_Customers` | Monthly customer count |
| `Menu_Price` | Average menu price ($) |
| `Marketing_Spend` | Marketing spend ($) |
| `Cuisine_Type` | American / Italian / Japanese / Mexican / Indian |
| `Average_Customer_Spending` | Average spending per customer ($) |
| `Seating_Capacity` | Number of seats |
| `Promotions` | Running promotions (0/1) |
| `Reviews` | Number of reviews |
| `Monthly_Revenue` | **Target** — monthly revenue ($) |

Full column-by-column explanation, EDA, and cleaning steps are in [`docs/PROJECT_EXPLANATION.md`](docs/PROJECT_EXPLANATION.md).

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/restaurant-revenue-predictor.git
cd restaurant-revenue-predictor

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage

The app loads its model files from the current working directory, so run it from the `model/` folder's parent, pointing at the right paths, or copy the `.pkl` files next to `app.py` (already the case in this repo layout below):

```bash
# From the project root, copy the model artifacts next to app.py once:
cp model/*.pkl .

# Then launch the app
streamlit run app.py
```

Open the local URL Streamlit prints (usually `http://localhost:8501`), fill in the restaurant's details, and click **Predict Revenue**.

To explore the full ML pipeline (EDA → cleaning → feature engineering → model comparison → tuning), open:

```bash
jupyter notebook notebooks/AI_Restaurant_Revenue_Prediction.ipynb
```

## 📈 Results

Six regression models were trained and compared:

| Rank | Model | MAE | RMSE | R² Score |
|---|---|---|---|---|
| 🥇 | **Linear Regression** | 3,782.15 | 4,715.90 | **0.9383** |
| 2 | Random Forest (Tuned) | 4,109.45 | 5,069.02 | 0.9287 |
| 3 | XGBoost | 4,155.43 | 5,095.98 | 0.9280 |
| 4 | Random Forest | 4,150.22 | 5,122.99 | 0.9272 |
| 5 | Decision Tree | 4,524.00 | 5,669.29 | 0.9109 |
| 6 | SVM (SVR) | 12,876.69 | 16,350.91 | 0.2585 |

**Linear Regression** was selected as the final model, deployed in `app.py`.

## 🏆 Model Performance

- **R² Score:** 0.9383 (explains ~94% of the variance in monthly revenue)
- **MAE:** ~$3,782 average absolute error
- **RMSE:** ~$4,716
- **5-Fold Cross Validation:** mean R² = 0.9259 (std = 0.006) — consistent and stable
- **Most important feature:** `Customers_x_Spending` (an engineered interaction term), accounting for ~94% of feature importance in the tuned Random Forest

Full metric definitions, math, and interpretation are in [`docs/PROJECT_EXPLANATION.md`](docs/PROJECT_EXPLANATION.md).

## 🚀 Future Improvements

- Collect richer, more realistic real-world data (location, rent, local competition, seasonality)
- Wrap preprocessing + model into a single `sklearn.Pipeline` to reduce train/serve mismatch risk
- Add prediction confidence intervals instead of a single point estimate
- Try LightGBM / CatBoost, especially for native categorical handling
- Add SHAP-based per-prediction explainability
- Add model monitoring for drift after deployment

See [`docs/PROJECT_EXPLANATION.md`](docs/PROJECT_EXPLANATION.md) §28 for the full list.

## 📸 Screenshots

> Add screenshots of the running app here.

`screenshots/app_home.png`
`screenshots/app_prediction.png`

## 👤 Author

## 👤 Author

**Mohamed Sobhy Salah** — [GitHub](https://github.com/m07hamed30-cpu)

Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 📄 License

This project is licensed under the [MIT License](LICENSE).

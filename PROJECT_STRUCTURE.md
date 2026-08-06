# Project Structure

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
│   └── (app screenshots go here)
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

## File-by-File Purpose

| Path | Purpose |
|---|---|
| `data/Restaurant_Revenue_Dataset.csv` | Raw historical restaurant data used to train and evaluate the model. Read by the notebook. |
| `notebooks/AI_Restaurant_Revenue_Prediction.ipynb` | The full ML pipeline: EDA, cleaning, feature engineering, encoding, train/test split, scaling, PCA exploration, training and comparing 5 regression models, cross-validation, hyperparameter tuning (GridSearchCV), feature importance, and saving the final artifacts. |
| `model/best_model.pkl` | The trained Linear Regression model (the best performer), saved with `joblib.dump`. Loaded by `app.py`. |
| `model/scaler.pkl` | The `StandardScaler` fitted on training data. Must be used (via `.transform()`, never re-fit) on any new input before prediction. |
| `model/feature_columns.pkl` | The exact list and order of feature columns the model was trained on. Used by `app.py` to build input rows correctly. |
| `app.py` | The Streamlit web app: collects restaurant details from the user, reproduces the same feature engineering and encoding used in training, scales the input, and returns a predicted monthly revenue. |
| `docs/PROJECT_EXPLANATION.md` | A complete, from-scratch, line-by-line explanation of the entire project (in Arabic) — intended as a study/discussion reference. |
| `requirements.txt` | Python package dependencies needed to run the notebook and the app. |
| `.gitignore` | Files and folders excluded from version control (caches, virtual environments, IDE files, etc.). |
| `LICENSE` | MIT License text. |
| `README.md` | Main project overview: description, installation, usage, results. |
| `CHANGELOG.md` | Version history of the repository. |
| `CONTRIBUTING.md` | Guidelines for contributing to the project. |
| `CODE_OF_CONDUCT.md` | Community behavior guidelines. |
| `PRESENTATION_NOTES.md` | Talking points for presenting/defending this project. |
| `FAQ.md` | Frequently asked questions about the project. |
| `INTERVIEW_QA.md` | Common technical interview questions related to this project, with model answers. |

## How the Files Connect

1. `data/Restaurant_Revenue_Dataset.csv` is read by `notebooks/AI_Restaurant_Revenue_Prediction.ipynb`.
2. The notebook processes the data end-to-end and, at the end, saves three artifacts via `joblib.dump()`: `best_model.pkl`, `scaler.pkl`, `feature_columns.pkl` — placed in `model/`.
3. `app.py` loads those three artifacts at startup (cached via `@st.cache_resource`), takes user input through a Streamlit form, reproduces the exact same feature engineering (`Customers_x_Spending`) and one-hot encoding used in the notebook, scales the input with the saved scaler, and calls `model.predict()`.
4. `docs/PROJECT_EXPLANATION.md` documents every step of this pipeline in detail for study or defense purposes.

> **Important:** any change to the feature set or preprocessing logic in the notebook must be mirrored exactly in `app.py`, or predictions will silently become incorrect.

# Interview Q&A

Common technical interview questions this project might prompt, with model answers.

---

**Q: Walk me through your ML pipeline end to end.**
A: Load data → EDA (shape, dtypes, describe, correlations, plots) → clean (fill missing `Marketing_Spend`/`Reviews` with median, drop 8 exact duplicates, remove outliers in `Monthly_Revenue` via IQR) → feature engineer `Customers_x_Spending` → one-hot encode `Cuisine_Type` with `drop_first=True` → split 80/20 with `random_state=42` → scale with `StandardScaler` (fit on train, transform on test) → explore PCA as a reference (not used in final model) → train and compare 5 regression models → 5-fold cross-validate → tune the Random Forest with `GridSearchCV` → select the best model by test R² (Linear Regression won) → save model, scaler, and feature columns with `joblib` → serve via Streamlit.

**Q: Why is this a regression problem and not classification?**
A: The target, `Monthly_Revenue`, is a continuous numeric value, not a discrete category.

**Q: How did you handle missing data, and why that method?**
A: Filled `Marketing_Spend` (10 missing) and `Reviews` (15 missing) with their column median rather than mean, since median is robust to outliers and won't be skewed by extreme values.

**Q: How did you detect and handle outliers?**
A: Used the IQR method on `Monthly_Revenue`: computed Q1, Q3, IQR = Q3-Q1, then removed rows outside `[Q1 - 1.5×IQR, Q3 + 1.5×IQR]`. This removed 8 rows.

**Q: What encoding did you use for the categorical column, and why?**
A: One-hot encoding via `pd.get_dummies(..., drop_first=True)`. `Cuisine_Type` is nominal (no inherent order), so one-hot is correct — label encoding would falsely imply an ordinal relationship between cuisines. `drop_first=True` avoids the dummy variable trap (perfect multicollinearity).

**Q: Why did you scale the features, and how?**
A: Used `StandardScaler` (z-score standardization: `(x - mean) / std`) because features have very different ranges (e.g., `Number_of_Customers` vs `Marketing_Spend`), and scale-sensitive models like Linear Regression and SVR need this to treat features fairly. Critically, `fit_transform` was applied only to training data; `transform` (not `fit_transform`) was applied to test data to avoid data leakage.

**Q: What's the difference between a parameter and a hyperparameter?**
A: A parameter is learned by the model during training (e.g., linear regression coefficients). A hyperparameter is set before training (e.g., `n_estimators`, `max_depth`, `learning_rate`) and controls how the model learns.

**Q: Explain the evaluation metrics you used.**
A: MAE (mean absolute error, same units as target, treats all errors equally), MSE (mean squared error, penalizes large errors more, but in squared units), RMSE (square root of MSE, back in original units while still penalizing large errors), and R² (proportion of variance in the target explained by the model, 1 = perfect, 0 = no better than predicting the mean).

**Q: Why did you use cross-validation in addition to a train/test split?**
A: A single train/test split can be sensitive to which rows happened to land in the test set. 5-fold cross-validation trains/evaluates the model 5 times on different splits and averages the results, giving a more reliable estimate and a sense of variance (via the standard deviation across folds).

**Q: How did you tune hyperparameters?**
A: `GridSearchCV` with 5-fold cross-validation over a grid of `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf` for Random Forest — an exhaustive search over all 36 combinations, scored by R².

**Q: Why did the simplest model (Linear Regression) outperform Random Forest and XGBoost?**
A: Because the engineered feature `Customers_x_Spending` captures the dominant, near-linear relationship driving revenue in this dataset. Once that relationship is (nearly) linear, a linear model fits it directly, while more flexible models don't gain an advantage and may even slightly overfit relative to the simpler model. This is a practical illustration of Occam's Razor — prefer the simplest model that performs as well.

**Q: How do you know your model isn't overfitting?**
A: Test set R² (0.9383) is close to the 5-fold cross-validation mean R² (0.9259), and the standard deviation across folds is small (0.006) — consistent performance across different data subsets, not a lucky split.

**Q: What is feature importance, and what did it tell you here?**
A: For tree-based models, it measures how much each feature contributed to reducing prediction error across all splits in all trees. Here, `Customers_x_Spending` alone accounted for ~94% of importance — by far the dominant driver of revenue in this dataset, while cuisine type and promotions had minimal impact.

**Q: How did you serialize and deploy the model?**
A: Used `joblib.dump()` to save the trained model, the fitted `StandardScaler`, and the exact list/order of feature columns as `.pkl` files. The Streamlit app (`app.py`) loads these once (cached with `@st.cache_resource`), reconstructs the same feature engineering and encoding for new user input, scales it with the saved scaler (`transform`, not `fit_transform`), and calls `model.predict()`.

**Q: What are the biggest risks or limitations of this model?**
A: The dominant reliance on `Customers_x_Spending` suggests the data may be closer to synthetic than fully real-world; important real factors like location, rent, competition, and seasonality aren't present. The linear model also doesn't constrain predictions to be non-negative, which could produce unrealistic outputs at extreme inputs.

**Q: What would you do differently, or improve, next?**
A: Wrap preprocessing and model into a single `sklearn.Pipeline` to eliminate train/serve mismatch risk, add prediction confidence intervals, try LightGBM/CatBoost for native categorical support, add SHAP-based explainability, and monitor for model drift once deployed on real-world data.

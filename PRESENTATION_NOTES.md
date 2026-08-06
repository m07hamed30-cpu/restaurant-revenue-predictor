# Presentation Notes

Quick talking points for presenting or defending this project.

## 30-Second Pitch

"Opening a restaurant is expensive, and owners want to estimate revenue before investing. We built a regression model trained on 1,192 historical restaurants that predicts expected monthly revenue from characteristics like customer count, menu price, and marketing spend — deployed as a live Streamlit app. Our best model (Linear Regression) explains 93.8% of the variance in revenue with an average error of about $3,782."

## Structure to Follow When Presenting

1. **Problem** — investment risk, no data-driven estimate available beforehand.
2. **Data** — 1,208 restaurants, 9 columns, target = `Monthly_Revenue`.
3. **Pipeline** — EDA → cleaning (missing values, duplicates, outliers) → feature engineering (`Customers_x_Spending`) → one-hot encoding → scaling → 5 models trained and compared.
4. **Key insight** — the engineered interaction feature `Customers_x_Spending` accounts for ~94% of feature importance; it's the dominant driver of revenue in this data.
5. **Model selection** — Linear Regression won (R²=0.9383) over more complex models (Random Forest, XGBoost) because the relationship became near-linear once the interaction term was added — a good example of Occam's Razor in ML.
6. **Validation** — 5-fold cross-validation confirmed stability (mean R²=0.9259, std=0.006), not a lucky split.
7. **Deployment** — Streamlit app reproduces the exact training-time preprocessing before calling `model.predict()`.
8. **Limitations & future work** — data may be closer to synthetic than fully real-world; no rent/location/competition features; future work includes richer data, `sklearn.Pipeline`, confidence intervals, SHAP explainability.

## Anticipate These Questions

- Why regression, not classification? → continuous target.
- Why did the "simplest" model win? → relationship is near-linear after feature engineering (see §21 in `docs/PROJECT_EXPLANATION.md`).
- How do you know it's not overfitting? → cross-validation + held-out test set both agree.
- What would you improve? → see `README.md` "Future Improvements" section.

## Suggested Slide Order

1. Title + problem statement
2. Dataset overview
3. EDA highlights (correlation heatmap, key scatter plots)
4. Cleaning & feature engineering
5. Model comparison table
6. Feature importance chart
7. Live demo of the Streamlit app
8. Limitations & future work

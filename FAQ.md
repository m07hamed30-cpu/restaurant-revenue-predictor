# Frequently Asked Questions (FAQ)

**Q: What does this project actually predict?**
A: The expected **monthly revenue** (in dollars) of a restaurant, given its characteristics (customer count, menu price, marketing spend, cuisine type, average customer spending, seating capacity, promotions, and review count).

**Q: What kind of model is used?**
A: The final deployed model is a **Linear Regression** model — it had the best R² score (0.9383) among six models compared (Linear Regression, Decision Tree, Random Forest, tuned Random Forest, XGBoost, SVR).

**Q: Why did a simple Linear Regression beat more advanced models like XGBoost?**
A: Because of an engineered feature, `Customers_x_Spending` (number of customers × average spending per customer), the relationship between the features and revenue became close to linear. Once that's true, a linear model can match or beat more complex, non-linear models — see §21 of `docs/PROJECT_EXPLANATION.md`.

**Q: How accurate is the model?**
A: On held-out test data: R² = 0.9383 (explains ~94% of the variance in revenue), MAE ≈ $3,782, RMSE ≈ $4,716. 5-fold cross-validation confirms this is stable (mean R² = 0.9259, std = 0.006).

**Q: What's the single most important factor in predicting revenue?**
A: `Customers_x_Spending`, accounting for ~94% of feature importance in the tuned Random Forest — i.e., how many customers a restaurant serves times how much each one spends.

**Q: Can I use this model for a real restaurant investment decision?**
A: It's a useful data-driven signal, but treat it as one input among many. The training data may not fully capture real-world factors like location, rent, local competition, or seasonality — see the "Limitations" note in §23 of `docs/PROJECT_EXPLANATION.md`.

**Q: How do I run the app locally?**
A: See the "Installation" and "Usage" sections in `README.md` — in short: `pip install -r requirements.txt` then `streamlit run app.py` (with the `.pkl` files alongside it).

**Q: Why are there missing values handled with the median instead of the mean?**
A: The median is more robust to outliers — it won't be pulled toward extreme values the way the mean can be.

**Q: Was PCA used in the final model?**
A: No. It was explored for reference (§14 of `docs/PROJECT_EXPLANATION.md`), but the feature set is already small and meaningful, and a direct comparison showed slightly better performance without PCA.

**Q: Where can I find a full explanation of every step?**
A: `docs/PROJECT_EXPLANATION.md` — a complete, from-scratch walkthrough of the entire pipeline, written as a study guide.

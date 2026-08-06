# Contributing

Thanks for considering a contribution to Restaurant Revenue Predictor!

## How to Contribute

1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Make your changes. If you modify the notebook or retrain the model, re-export:
   - `model/best_model.pkl`
   - `model/scaler.pkl`
   - `model/feature_columns.pkl`
   and update `app.py` if the feature set or preprocessing changes.
4. Test that `streamlit run app.py` still runs end-to-end without errors.
5. Commit with a clear message and open a Pull Request describing what changed and why.

## Reporting Issues

Please open an issue with:
- A clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, Python version, package versions)

## Code Style

- Follow PEP 8 for Python code.
- Keep notebook cells focused and well-labeled with markdown headers, consistent with the existing structure (EDA → Cleaning → Feature Engineering → Encoding → Split → Scaling → Training → Evaluation → Tuning → Saving).

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

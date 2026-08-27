# ✈️ British Airways Reviews — Sentiment Analysis

This repository performs sentiment analysis on passenger reviews for British Airways to help quantify customer satisfaction, surface recurring themes, and classify text feedback as positive, negative, or neutral.

---

## Project summary

This project demonstrates an end-to-end Natural Language Processing (NLP) workflow applied to real customer reviews scraped from Skytrax (AirlineQuality). The analysis covers:

- Data acquisition (web scraping)
- Data cleaning and preprocessing (tokenization, stopword removal, normalization)
- Feature extraction using classical NLP and transformer-based approaches
- Model training, evaluation and comparison (logistic regression and transformer embeddings)
- Visualizations and reporting (word clouds, sentiment distribution, trends)

The goal is to provide actionable insights for stakeholders (product managers, customer-experience teams, data scientists) who want to understand passenger sentiment and key pain points.

---
## Graphical overview


---

## Key results

- Reviews are classified into positive, negative, and neutral categories.
- Visualizations include sentiment distribution, common keywords per sentiment, and word clouds to highlight frequent terms.
- A baseline model (Logistic Regression) is implemented; transformer-based features are used as an optional higher-performing alternative.

---

## Structure

```
British-Airways-Reviews-Sentiment-Analysis/
  ├── data/                             # Raw and cleaned review data (CSV/JSON)
  ├── demo/                             # Small demo artifacts and GIFs for the README
  ├── plots/                            # Generated plots and images
  ├── reports/                          # Written report and result export
  ├── analysis.ipynb                    # Jupyter notebook: EDA, visualizations, experiments
  ├── cleaning_data.py                  # Script: clean and normalize raw reviews
  ├── extract_data.py                   # Script: scrape reviews from Skytrax
  ├── sentiment_analysis.py             # Script: train/evaluate classification models
  ├── requirements.txt                  # Python dependencies
  └── README.md                         # Project overview (this file)
```

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/MoshoodSO/British-Airway-Reviews-Sentiment-Analysis.git
   cd British-Airway-Reviews-Sentiment-Analysis
   ```

2. Create a virtual environment (recommended) and install dependencies:

    ```
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
    ```

If you don't have a GPU, the transformer models will run on CPU (slower). You can comment out transformer-related sections in the notebook or scripts if you want to run faster with classical features only.

---

## Usage

There are two main ways to run the analysis: via the Jupyter notebook for exploratory work, or running the scripts for reproducible runs.

- Notebook (recommended for exploration):
  1. Start Jupyter: `jupyter notebook` or `jupyter lab`
  2. Open `analysis.ipynb` and run cells sequentially.

- Command line (scripts):
  1. Collect data: `python extract_data.py --output data/raw_reviews.csv`
  2. Clean data: `python cleaning_data.py --input data/raw_reviews.csv --output data/clean_reviews.csv`
  3. Train & evaluate: `python sentiment_analysis.py --input data/clean_reviews.csv --model-output models/` 

Script arguments may vary — open the top of each script to see available CLI flags.

---

## Data source and ethics

- Source: Reviews were collected from Skytrax (AirlineQuality): [British Airways](https://www.airlinequality.com/airline-reviews/british-airways/)
- Note: If you plan to reproduce this work, check the site’s robots.txt and terms of service. Use scraped data responsibly and respect copyright and privacy.
- The repository contains no personal data other than the publicly-posted review text. If you extend this project, consider anonymization best practices.

---

## Methodology 

1. Data collection
   - Reviews are scraped from the British Airways page on Skytrax using `extract_data.py`.

2. Preprocessing
   - Typical steps implemented in `cleaning_data.py` include: lowercasing, HTML removal, punctuation removal, tokenization, stopword removal, and optional stemming/lemmatization.
   - Additional cleaning for this domain: removing short non-informative reviews, handling non-English content, and normalizing common airline-specific tokens (e.g., flight numbers).

3. Feature engineering
   - Baseline: TF-IDF vectors (unigrams/bigrams)
   - Optionally: pretrained transformer embeddings (from Hugging Face models) to capture semantic context

4. Modeling
   - Baseline classifier: Logistic Regression with cross-validation
   - Additional models: SVM, Random Forests, or fine-tuned transformer models (if compute permits)

5. Evaluation
   - Metrics: accuracy, precision, recall, F1 score (per-class and macro), and confusion matrix
   - Visualizations: distribution plots, word clouds per sentiment class, and time-based sentiment trends if timestamps exist

---

## Reproducing results and tips

- For stable results, set random seeds in the notebook/scripts (numpy, random, and sklearn seeding).
- If using transformer embeddings, cache model outputs to disk so you do not recompute embeddings each run.
- Use stratified sampling when creating train/test splits because classes can be imbalanced.

---

## Dependencies

Key libraries used (see `requirements.txt` for full, pinned versions):

- pandas, numpy
- scikit-learn
- nltk (tokenization, stopwords)
- matplotlib, seaborn, wordcloud
- transformers (optional — for transformer embeddings)

---

## What you can add / next steps

- Improve scraping to collect richer metadata (dates, ratings, route, cabin class)
- Add a model interpretability step (LIME/SHAP) to explain predictions
- Fine-tune a transformer model for better performance
- Build a simple dashboard (Streamlit or Dash) for interactive exploration

---

## Author

Developed by Shoyombo Moshood O. — ![LinkedIn](https://linkedin.com/in/shoyombo-moshood-582003126/)

For questions, feature requests, or contributions, please open an issue or create a PR.

---

## License

This repository currently has no explicit license file. If you want to open-source it, consider adding a LICENSE (for example, MIT) to clarify reuse terms.

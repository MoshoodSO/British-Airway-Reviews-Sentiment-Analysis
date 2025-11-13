## ✈️ British Airway Reviews Sentiment Analysis

This project performs sentiment analysis on customer reviews of *British Airways* to:

- Understand overall passenger satisfaction  
- Identify key themes in customer feedback  
- Classify reviews as *positive*, *negative*, or *neutral*
- Analyse the reviews feedback to get more insights

The review data was *scraped from the British Airways section* of the [Skytrax airline review website](https://www.airlinequality.com/airline-reviews/british-airways/), a popular platform for airline service ratings and passenger experiences.


## 📌 Objective

The primary goal of this project is to perform *sentiment analysis* on customer reviews of *British Airways* using *Natural Language Processing (NLP)* and *machine learning techniques*. Specifically, the project aims to:

- Analyze large volumes of textual feedback from passengers  
- Preprocess and clean raw review data for effective modeling  
- Use NLP techniques to extract meaningful insights and identify frequently mentioned keywords or themes  
- Build and evaluate classification models to categorize reviews as *positive*, *negative*, or *neutral*  
- Help uncover patterns and trends in customer satisfaction over time  
- Support airline decision-makers in improving services based on data-driven feedback

This project demonstrates how text mining and sentiment classification can provide valuable insights into customer experience in the aviation industry.


---

## 📂 Project Structure

```
British-airways-reviews-sentiment-analysis/
  ├── data/                             # Raw and cleaned review data
  ├── plots/                            # Evaluation metrics, visualisations
  ├── analysis.ipynb                    # Jupyter notebooks for EDA, and other visualisations
  ├── cleaning_data.py                  # Python script for cleaning and organising the raw data
  ├── extract_data.py                   # Python script for the scrapping of data from the web page
  ├── sentiment_analysis.py             # Python script for the sentiment analysis
  ├── requirements.txt                  # List of dependencies
  └── README.md                         # Project overview
```

## 🧪 Techniques & Tools Used

- *Python* (Pandas, NumPy, Scikit-learn)
- *NLP*: NLTK, transformer
- *ML Models*: Logistic Regression, Naive Bayes, or others
- *Visualization*: Matplotlib, Seaborn, WordCloud
- *Jupyter Notebook* for development and testing


## 📈 Process Overview

1. *Data Collection*: British Airways review dataset
2. *Text Preprocessing*: Tokenization, stopword removal, stemming/lemmatization
3. *Exploratory Data Analysis (EDA)*: Common words, review lengths, sentiment distribution
4. *Feature Engineering*: transformer
5. *Visualization*: Word clouds, sentiment trends

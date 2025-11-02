# Import packages
import pandas as pd
import numpy as np
import re


# Importing the dataframe
df = pd.read_csv("data/clean_british_airways_reviews.csv", index_col=[0])
# Display the first few rows of the dataframe
print(df.head())

# Stripping leading and trailing whitespace from the 'date' column
df["date"] = df["date"].str.strip()
df['date'] = pd.to_datetime(df['date'], errors='coerce')


# Cleaning "content" column by removing extra spaces and new lines
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# cleaning the comments
df['clean_comment'] = df.comment.apply(clean_text)


# length of words in "comment" column
df['content_length'] = df['clean_comment'].apply(lambda x: len(x) if pd.notnull(x) else 0)

# number of tokens in "comment" column
df['token_length'] = df['clean_comment'].apply(lambda x: len(x.split()) if pd.notnull(x) else 0)


# Sentiment analysis
# importing transformers for sentiment analysis on content column
from transformers import pipeline
# Create a sentiment-analysis pipeline
sentiment = pipeline('sentiment-analysis', device=0)

# Tokenizer import
from transformers import AutoTokenizer
# instantiate the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Function to truncate text to fit model token limit (510 tokens to allow for special tokens)
def truncate_to_model_tokens(text, max_tokens=510):
    tokens = tokenizer.tokenize(text)
    truncated = tokenizer.convert_tokens_to_string(tokens[:max_tokens])
    return truncated

# Apply truncation to content column
df["clean_comment_short"] = df["clean_comment"].apply(lambda x: truncate_to_model_tokens(x) if pd.notnull(x) else "")

# Apply sentiment analysis to the truncated content column and store results in a new column 
df["reviews_sentiment"] = df["clean_comment_short"].apply(lambda x: sentiment(x)[0]['label'] if pd.notnull(x) and x else None)
df["reviews_sentiment_score"] = df["clean_comment_short"].apply(lambda x: sentiment(x)[0]['score'] if pd.notnull(x) and x else None)

# Drop the temporary 'content_short' column
df1 = df.drop(columns=["clean_comment_short"])

# Exporting the dataframe with sentiment analysis to a new CSV file
df1.to_csv("data/clean_british_airways_reviews_with_sentiment_report.csv")

# Indicating completion of the sentiment analysis and exporting process
print("Done sentiment analysis and exporting the data!!!")

# End of code

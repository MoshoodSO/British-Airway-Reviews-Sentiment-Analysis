# Import packages
import pandas as pd
import numpy as np
import re


# Importing the dataframe
df = pd.read_csv("data/british_airways_reviews.csv")
print(df.shape)

# Display the first few rows of the dataframe
print(df.head())

# Splitting the 'title' column into 'name' and 'title' based on the first occurrence of '('
df[['name', 'title']] = df['title'].str.split('(', n=1, expand=True)

# Splitting the 'title' column into 'country' and 'date' based on the first occurrence of ')'
df[['country', 'date']] = df['title'].str.split(')', n=1, expand=True)

# Filtering the dataframe to include only rows where the 'verified' column matches the last unique value in that column
print(index_ := df[df["verified"] == df["verified"].unique()[-1]].index)

# Merging the 'verified' column content into the 'content' column for the specific row index 3587
content_ = [df.loc[index_[0], "verified"], df.loc[index_[0], "content"]]
df.loc[index_[0], "content"] = ' '.join(content_)
df.loc[index_[0], "verified"] = np.nan

# Cleaning the 'verified' column by removing specific leading characters
df["verified"] = df["verified"].str.lstrip("✅\n|c\n|❎\n")
print(df["verified"].value_counts(dropna=False))

# Stripping leading and trailing whitespace from the 'content' column
df["content"] = df["content"].str.strip()






# Creating a new dataframe with selected columns
df = df[['date', 'name', 'country', 'verified', 'content']]



##### Cleaning the "content" column
# separating the "comment" column
df[["comment", 'content']] = df['content'].str.split('\n', n=1, expand=True)

# creating and getting the "Seat Type" column from the "content" column
df[["content", 'seat_type']] = df['content'].str.split('Seat Type\n', n=1, expand=True)
# cleaning the "seat_type" column
df[['seat_type', "content2"]] = df['seat_type'].str.split('\n', n=1, expand=True)


# merging the created content columns and dropping one of them
df["content"] = df["content"] + df["content2"]
df = df.drop(["content2"], axis = 1)

# creating and getting the "type_of_traveller" column from the "content" column
df[["content", 'type_of_traveller']] = df['content'].str.split('Type Of Traveller\n', n=1, expand=True)
# cleaning the "type_of_traveller" column
df[['type_of_traveller', "content2"]] = df['type_of_traveller'].str.split('\n', n=1, expand=True)

# merging the created content columns and dropping one of them
df["content"] = df["content"] + df["content2"]
df = df.drop(["content2"], axis = 1)

# creating and getting the "route" column from the "content" column
df["route"] = df['content'].str.split('Route\n', n=1, expand=True)[1]
# cleaning the "route" column
df["route"] = df['route'].str.split('\n', n=1, expand=True)[0]

# final dataframe for export
df1 = df.drop(["content"], axis = 1)

# Exporting the cleaned dataframe to a new CSV file
df1.to_csv("data/clean_british_airways_reviews.csv")
print(df1.head())



# Indicating completion of the cleaning and exporting process
print("Done cleaning and exporting the data!!!")
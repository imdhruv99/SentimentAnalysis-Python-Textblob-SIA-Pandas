import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# File Location and Selected Columns
file_location = '../Dataset/Dataset1.xlsx'
cols = [0, 4]

# Reading Data using Pandas
data = pd.read_excel(file_location, usecols=cols)

# Labeling Our Data
sia = SentimentIntensityAnalyzer()
results = []

for item in data['Title']:
    pol_score = sia.polarity_scores(item)
    pol_score['Headline'] = item
    results.append(pol_score)

# DataFrames
data = pd.DataFrame.from_records(results)

# Creating Label
data['label'] = "Neutral"
data.loc[data['compound'] > 0.2, 'label'] = "Positive"
data.loc[data['compound'] < -0.2, 'label'] = "Negative"


data2 = data[['Headline', 'label']]
data2.to_excel('../Dataset/Result/SentimentIntensityAnalyzer/Result-Dataset1.xlsx')




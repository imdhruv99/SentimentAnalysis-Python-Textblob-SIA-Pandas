import pandas as pd
from textblob import TextBlob

# File Location and Selected Columns
file_location = '../Dataset/Dataset1.xlsx'
cols = [0, 4]

# Reading Data using Pandas
data = pd.read_excel(file_location, usecols=cols)

# Polarity and Subjectivity
polarity = lambda title: TextBlob(title).sentiment.polarity

data['Polarity'] = data['Title'].apply(polarity)


# Creating Label
data['label'] = "Neutral"
data.loc[data['Polarity'] >= 0.1, 'label'] = "Positive"
data.loc[data['Polarity'] <= -0.1, 'label'] = "Negative"


data2 = data[['Title', 'label']]
data2.to_excel("../Dataset/Result/Textblob/Result-Dataset1.xlsx")

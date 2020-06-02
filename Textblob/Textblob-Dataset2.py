import pandas as pd
from textblob import TextBlob

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid', context='talk', palette='Dark2')

# File Location and Selected Columns
file_location = '../Dataset/Dataset2.xlsx'
cols = [0, 4]

# Reading Data using Pandas
data = pd.read_excel(file_location, usecols=cols)

# Polarity and Subjectivity
polarity = lambda title: TextBlob(title).sentiment.polarity
# subjectivity = lambda title: TextBlob(title).sentiment.subjectivity


data['Polarity'] = data['Title'].apply(polarity)
# data['Subjectivity'] = data['Title'].apply(subjectivity)

# Creating Label
data['label'] = "Neutral"
data.loc[data['Polarity'] >= 0.1, 'label'] = "Positive"
data.loc[data['Polarity'] <= -0.1, 'label'] = "Negative"


data2 = data[['Title', 'label']]

data2.to_excel("../Dataset/Result/Textblob/Result-Dataset2.xlsx")

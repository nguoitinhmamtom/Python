# Exercise 1:
# Read the file scores.csv into a DataFrame and check the structure dataset.
# From the DataFrame
# Sort and display the teams in ascending order based on score.
# Sort and display the teams in ascending order based on category, then by score.
# Calculate the mean of score for all teams in the dataset.
# Filter the teams with scores greater than 80 and display them in descending order of year.
# Create a new column score_plus_10 by adding 10 to the score column.
# Create a new column score_ratio by calculating the ratio of score to the maximum score in the dataset.
# How would you filter the data to include only teams with a category of 'A' or 'B' and score greater than 75?
# How would you group the dataset by category and calculate the sum of score for each category?

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
df_scores = pd.read_csv('/content/drive/MyDrive/Dataset/scores.csv')
df_scores.head(5)
df_scores.tail(5)
df_scores.sample(5)
df_scores.shape
df_scores.info()
df_scores.describe()
df_scores.sort_values('score')
df_scores.sort_values(['category','score'])
df_scores['mean_of_score'] = df_scores['score'].mean()
df_new_scores = df_scores[(df_scores['score']>80)]
df_new_scores.sort_values('year', ascending = False)
df_scores['score_plus_10'] = df_scores['score'] + 10
df_scores['score_ratio'] = df_scores['score']/df_scores['score'].max()
df_new1_scores = df_scores[df_scores['category'].isin(['A','B'])]
df_new1_scores[df_new1_scores['score']>70]
df_scores.groupby('category')['score'].sum().reset_index()
df_scores.groupby('category')['score'].agg(total = 'sum').reset_index()
df_scores.groupby('category').agg(total = ('score','sum')).reset_index()

# Exercise 2:
# Read file euro_2012.csv into a DataFrame and check information by using info().
# From the DataFrame:
# Filter 6 columns Team, Goals, Yellow Cards, Red Cards, Passes and Players Used.
# Sort and display teams in the ascending order of 'Player Used'.
# Sort and display teams in the ascending orders of 'Yellow Cards' and 'Red Cards' respectively
# Calculate the mean of 'Yellow Cards' of all teams in Euro 2012
# Filter teams having more than 9 goals and sort them in the descending order of 'Passes'
# Create a new column 'Shooting Accuracy' as ['Shots on target'] / (['Shots on target'] + ['Shots off target']) * 100
# Sort and display teams, goals and shooting accuracy in the descending order of 'Shooting Accuracy'

import pandas as pd
df_euro = pd.read_csv('/content/drive/MyDrive/Dataset/euro_12.csv')
df_euro1 = df_euro[['Team', 'Goals', 'Yellow Cards', 'Red Cards', 'Passes', 'Players Used']]
df_euro1
df_euro1.sort_values('Players Used')
df_euro1.sort_values(['Yellow Cards','Red Cards'])
df_euro1['Yellow Cards'].mean()
df_euro2 = df_euro1[df_euro1['Goals']>9]
df_euro2.sort_values('Passes', ascending = False)
df_euro['Shooting Accuracy'] = df_euro['Shots on target'] / (df_euro['Shots on target'] + df_euro['Shots off target']) * 100
df_euro.sort_values('Shooting Accuracy', ascending = False)[['Team','Goals','Shooting Accuracy']]

# Exercise 3:
# Read file users.txt into a DataFrame and check information by using info().
# From the DataFrame:
# Calculate mean of ages for each occupation
# Calculate male ratio (%) of each occupation
# Sort male ratios in descending order
# Find and display min and max ages of each occupation
# Calculate and display mean of ages of male and female for each occupation
# Count and display occupations by gender (male and female)

import pandas as pd
from scipy.stats import ttest_ind, norm

# Load your data
data = pd.read_csv("output.csv")

# Hypothesis 1: Games availible in multi player vs single player
# 'multiplayer' indicates if it's available on multiple platforms (0 = single, 1 = multiple)
data['platform_type'] = data['multiplayer'].apply(lambda x: 'Multiple' if x > 0 else 'Single')
multi_platform_scores = data[data['platform_type'] == 'Multiple']['average_score']
single_platform_scores = data[data['platform_type'] == 'Single']['average_score']

# Performing two-sample t-test
t_stat, p_value = ttest_ind(multi_platform_scores, single_platform_scores, equal_var=False)
print(f"Two-sample t-test for Hypothesis 1 (multi vs. single platform):\nT-statistic: {t_stat}\nP-value: {p_value}")

# Hypothesis 2: Action games have higher scores
# Assuming 'Genre1' of 5 represents Action games
#NEED TO CHANGE
action_scores = data[data['Genre1'] == 5]['average_score']
non_action_scores = data[data['Genre1'] != 5]['average_score']

# Performing two-sample t-test
t_stat, p_value = ttest_ind(action_scores, non_action_scores, equal_var=False)
print(f"\nTwo-sample t-test for Hypothesis 2 (Action vs. non-Action games):\nT-statistic: {t_stat}\nP-value: {p_value}")

#Hypothesis 2.1 (Not sure which would make more sense?)


action_data = data[data['Genre1'] == 8]  # Assuming '8' is the code for Action games

# Calculate the sample mean for Action games
action_mean = action_data['average_score'].mean()


population_mean = data['average_score'].mean() 
population_std = data['average_score'].std() / (len(data['average_score']) ** 0.5)  

# Perform the one-sample z-test
z_score = (action_mean - population_mean) / population_std
p_value = norm.sf(abs(z_score)) * 2  # two-tailed test

print(f"Hypothesis 2.1 Z-score: {z_score}")
print(f"Hypothesis 2.1 P-value: {p_value}")

#hypothesis 3

# Define high and low groups based on median
median_reviews = data['rating_count'].median()
high_review_data = data[data['rating_count'] > median_reviews]['average_score']
low_review_data = data[data['rating_count'] <= median_reviews]['average_score']

# Performing two-sample t-test
t_stat, p_value = ttest_ind(high_review_data, low_review_data, equal_var=False)
print(f"Two-sample t-test for high vs. low review counts:\nT-statistic: {t_stat}\nP-value: {p_value}")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor  # Import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("output.csv")

# Handle Missing Values
imputer = SimpleImputer(strategy='mean')
data = data.dropna()  # Drops rows with missing values for other columns
data[['average_score']] = imputer.fit_transform(data[['average_score']])

# Feature Engineering
# Convert categorical variables to numerical representations 
# maybe (one-hot encoding for genres and companies)
data = pd.get_dummies(data, columns=["Genre1", "Genre2", "Genre3", "Genre4", "Genre5"])

# Initial Investigation
# 1. Correlation between genre and success
numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
genre_correlation = data[numeric_columns].corr()['average_score']
print("\nCorrelation between genre and average score:")
print(genre_correlation)

# # Plotting Correlation between genre and average score using a heatmap
# Needs improvement before final deliverable
# plt.figure(figsize=(10, 8))
# sns.heatmap(genre_correlation.to_frame(), cmap='coolwarm', annot=True, fmt=".2f", cbar=False)
# plt.title('Correlation between Genre and Average Score')
# plt.xlabel('Genre')
# plt.ylabel('Average Score')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# 2. Platform influence on success (based on involved companies 1, 2 from the csv)
involved_companies = ['Involved_company1', 'Involved_company2']
platform_influence = pd.concat([data[company] for company in involved_companies if company in data.columns])
platform_influence = platform_influence.value_counts().sort_values(ascending=False).head(10)
print("\nPlatform influence based on involved companies:")
print(platform_influence)

# Plotting Platform influence based on involved companies using a bar plot
#Need to get Company names rather than ID to make the data more relevant
plt.figure(figsize=(10, 6))
platform_influence.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Platforms Influencing Success')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Relationship between user reviews and success
user_review_correlation = data[['average_score', 'rating', 'rating_count']].corr()['average_score'].sort_values(ascending=False)
print("\nCorrelation between user reviews and average score:")
print(user_review_correlation)

#Plotting needs improvement
# # Plotting Relationship between user reviews and average score using scatter plots
# fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# axes[0].scatter(data['rating'], data['average_score'], alpha=0.5, color='blue')
# axes[0].set_title('Rating vs. Average Score')
# axes[0].set_xlabel('Rating')
# axes[0].set_ylabel('Average Score')

# axes[1].scatter(data['rating_count'], data['average_score'], alpha=0.5, color='green')
# axes[1].set_title('Rating Count vs. Average Score')
# axes[1].set_xlabel('Rating Count')
# axes[1].set_ylabel('Average Score')
# plt.tight_layout()
# plt.show()

# Split Data
X = data.drop(["game_name", "id", "name", "average_score"], axis=1)
y = data["average_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Supervised Regression (Linear Regression)
# Model Training
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Model Evaluation
regression_predictions = regression_model.predict(X_test)
regression_mae = mean_absolute_error(y_test, regression_predictions)
regression_mse = mean_squared_error(y_test, regression_predictions)
regression_rmse = np.sqrt(regression_mse)
regression_r2 = r2_score(y_test, regression_predictions)

print("\nLinear Regression Results:")
print("Mean Absolute Error (MAE):", regression_mae)
print("Mean Squared Error (MSE):", regression_mse)
print("Root Mean Squared Error (RMSE):", regression_rmse)
print("R-squared (R2) Score:", regression_r2)

# Cross-Validation
regression_cv_scores = cross_val_score(regression_model, X, y, cv=5, scoring='neg_mean_squared_error')
regression_cv_rmse_scores = np.sqrt(-regression_cv_scores)
print("\nCross-Validation RMSE Scores:", regression_cv_rmse_scores)

# Regularized Regression (Ridge Regression)
ridge_model = Ridge(alpha=1.0)  # Increased alpha parameter
ridge_model.fit(X_train, y_train)
#evaluating...
ridge_predictions = ridge_model.predict(X_test)
ridge_mae = mean_absolute_error(y_test, ridge_predictions)
ridge_mse = mean_squared_error(y_test, ridge_predictions)
ridge_rmse = np.sqrt(ridge_mse)
ridge_r2 = r2_score(y_test, ridge_predictions)

print("\nRidge Regression Results:")
print("Mean Absolute Error (MAE):", ridge_mae)
print("Mean Squared Error (MSE):", ridge_mse)
print("Root Mean Squared Error (RMSE):", ridge_rmse)
print("R-squared (R2) Score:", ridge_r2)

# Cross-Validation Results
ridge_cv_scores = cross_val_score(ridge_model, X, y, cv=5, scoring='neg_mean_squared_error')
ridge_cv_rmse_scores = np.sqrt(-ridge_cv_scores)
print("\nCross-Validation RMSE Scores:", ridge_cv_rmse_scores)

# Supervised Regression (Random Forest Regression)
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)  # Initialize RandomForestRegressor
random_forest_model.fit(X_train, y_train)
random_forest_predictions = random_forest_model.predict(X_test)
random_forest_mae = mean_absolute_error(y_test, random_forest_predictions)
random_forest_mse = mean_squared_error(y_test, random_forest_predictions)
random_forest_rmse = np.sqrt(random_forest_mse)
random_forest_r2 = r2_score(y_test, random_forest_predictions)

print("\nRandom Forest Regression Results:")
print("Mean Absolute Error (MAE):", random_forest_mae)
print("Mean Squared Error (MSE):", random_forest_mse)
print("Root Mean Squared Error (RMSE):", random_forest_rmse)
print("R-squared (R2) Score:", random_forest_r2)

# Cross-Validation
random_forest_cv_scores = cross_val_score(random_forest_model, X, y, cv=5, scoring='neg_mean_squared_error')
random_forest_cv_rmse_scores = np.sqrt(-random_forest_cv_scores)
print("\nCross-Validation RMSE Scores:", random_forest_cv_rmse_scores)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the data
data = pd.read_csv("output.csv")

# Handle Missing Values
imputer = SimpleImputer(strategy='mean')
data = data.dropna()  # Drops rows with missing values for other columns
data[['average_score']] = imputer.fit_transform(data[['average_score']])

# Convert original_release_date to number of days since the first release date
data['original_release_date'] = pd.to_datetime(data['original_release_date'])
data['original_release_date'] = (data['original_release_date'] - data['original_release_date'].min()).dt.days

# Feature Engineering
data = pd.get_dummies(data, columns=["Genre1", "Genre2", "Genre3", "Genre4", "Genre5"])

# Initial Investigation
numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
genre_correlation = data[numeric_columns].corr()['average_score']

# Platform influence on success
involved_companies = ['Involved_company1', 'Involved_company2']
platform_influence = pd.concat([data[company] for company in involved_companies if company in data.columns])
platform_influence = platform_influence.value_counts().sort_values(ascending=False).head(10)

# Relationship between user reviews and success
user_review_correlation = data[['average_score', 'rating', 'rating_count']].corr()['average_score'].sort_values(ascending=False)

# Split Data
X = data.drop(["game_name", "id", "name", "average_score"], axis=1)
y = data["average_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Supervised Regression (Linear Regression)
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
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
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

# Supervised Regression (Random Forest Regression) with enhanced parameters
random_forest_model = RandomForestRegressor(n_estimators=1000, max_depth=20, min_samples_split=2, min_samples_leaf=1, random_state=42)  

# Cross-Validation
random_forest_cv_scores = cross_val_score(random_forest_model, X, y, cv=5, scoring='neg_mean_squared_error')
random_forest_cv_rmse_scores = np.sqrt(-random_forest_cv_scores)

# Print the cross-validation RMSE scores
print("\nCross-Validation RMSE Scores:", random_forest_cv_rmse_scores)

# Train the model
random_forest_model.fit(X_train, y_train)

# Predictions
random_forest_predictions = random_forest_model.predict(X_test)

# Model Evaluation
random_forest_mae = mean_absolute_error(y_test, random_forest_predictions)
random_forest_mse = mean_squared_error(y_test, random_forest_predictions)
random_forest_rmse = np.sqrt(random_forest_mse)
random_forest_r2 = r2_score(y_test, random_forest_predictions)

# Print the evaluation metrics
print("\nImproved Random Forest Regression Results:")
print("Mean Absolute Error (MAE):", random_forest_mae)
print("Mean Squared Error (MSE):", random_forest_mse)
print("Root Mean Squared Error (RMSE):", random_forest_rmse)
print("R-squared (R2) Score:", random_forest_r2)

# Visualization 1: Correlation Heatmap
data = data.drop('franchise_len', axis=1)
numeric_data = data.select_dtypes(include=[np.number])  # Select only numeric columns
print(numeric_data.columns)
plt.figure(figsize=(10, 7))

sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Visualization 2: Platform Influence on Success
plt.figure(figsize=(10, 6))
platform_influence.sort_values().plot(kind='barh', color=sns.color_palette("Set2", len(platform_influence)))
plt.title('Top 10 Platforms by Involvement Count')
plt.xlabel('Involvement Count')
plt.ylabel('Platform')
plt.show()

# Visualization 3: Relationship Between User Reviews and Success
plt.figure(figsize=(10, 6))
user_review_correlation_sorted = user_review_correlation.sort_values(ascending=False)
sns.barplot(y=user_review_correlation_sorted.values, x=user_review_correlation_sorted.index, palette='magma')
plt.title('Correlation to User Reviews')
plt.xlabel('Feature')
plt.ylabel('Percentage')
plt.show()

# Visualization 4: Model Performance Comparison
metrics = ['MAE', 'RMSE', 'R-squared']
model_metrics = {
    'Linear Regression': [regression_mae, regression_rmse, regression_r2],
    'Ridge Regression': [ridge_mae, ridge_rmse, ridge_r2],
    'Random Forest Regression': [random_forest_mae, random_forest_rmse, random_forest_r2]
}

plt.figure(figsize=(10, 6))
bar_width = 0.25
index = np.arange(len(metrics))

for i, (model, metric_values) in enumerate(model_metrics.items()):
    plt.bar(index + i * bar_width, metric_values, bar_width, label=model)

plt.xlabel('Metrics')
plt.ylabel('Values')
plt.title('Model Performance Comparison')
plt.xticks(index + bar_width, metrics)
plt.legend()
plt.show()

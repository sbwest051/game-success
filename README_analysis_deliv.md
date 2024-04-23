**ANALYSIS DELIVERABLE**

## Question 1
Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
**ML Component:**
We chose Linear Regression and Random Forest as our ML models and Ridge Regression to mitigate any overfitting.

**Linear Regression:** It's a more simple and effective technique suitable for predicting a continuous target variable (in this case, the average score of video games). It's a good starting point for understanding the linear relationship between features and the target variable.

**Random Forest:**  Random forest regression is capable of capturing non-linear relationships between features and the target variable. It does this by constructing multiple decision trees and averaging their predictions, making it well-suited for complex datasets with non-linear patterns. It can also handle a large number of input variables and is robust to outliers and noisy data. It also automatically handles feature selection, reducing the need for extensive feature engineering.

**Ridge Regression:** Since we have multiple features like genres, reviews, developing companies, etc (including categorical variables transformed into dummy variables) ridge regression can help mitigate potential overfitting by introducing regularization. It adds a penalty term to the regression coefficients, which can prevent extreme values and make the model more trust-worthy.

There are for sure more robust techniques or complex supervised models that we coud have employed, however, we did not feel prepared on the conceptual and technical side to use things such as Gradient Boosting or other types of regressions.

**Metrics Used for Evaluation:**
Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) were used to measure the accuracy of predictions.
R-squared (R2) Score was used to assess the goodness of fit of the models.

**Challenges**
Although we've mostly learned about K-means, which is used for clustering data 
into groups based on similarity. Our goal of prediction requires using a continuous 
target variable (average score) based on features, making it more of a supervised 
learning problem. So we had to learn more, both technically and conceptually, 
about topics that were briefly discussed in lecture such as random forests and 
other methods for regularzation. 

We also had to deal with missing values and data cleaning. 
For example, categorical variables such as genres and involved companies, 
needed to be converted into numerical representations for modeling.
One-hot encoding was employed using pd.get_dummies() to convert categorical 
variables into binary vectors. 
SimpleImputer with the strategy of replacing missing values with the mean was 
used (strategy='mean'). Additionally, rows with missing values for other columns 
were dropped using data.dropna(). These steps ensure that missing values are 
addressed, enabling a cleaner dataset for analysis and modeling.
Also interpreting the coefficients in Ridge Regression was more complex 
compared to Linear Regression, but by using the provided regularization parameter 
(alpha) twe can control the amount of shrinkage applied to the coefficients. 
By tuning this, we can balance between simplicity and model complexity, 
enabling better interpretation of the coefficients.


## Question 2
What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?
- ML Component: 


## Question 3
Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?
Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?
Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?
- ML Component: 
**Results**
Linear Regression: The R-squared value of 0.215 suggests that the model explains only 21.5% of the variance in the target variable. The mean absolute error (MAE) of 0.131 indicates that, on average, the model's predictions are off by approximately 0.131 units from the actual values.
Ridge Regression: The R-squared value slightly improved to 0.225 compared to linear regression, indicating a marginal enhancement in model performance. The mean absolute error and other evaluation metrics are similar to those of linear regression.
Random Forest Regression: The R-squared value improved further to 0.247, indicating better performance compared to the linear and ridge regression models. The mean absolute error also decreased slightly to 0.127, suggesting that random forest regression provides the best predictive performance among the models tested.

**Interpretation of results**
The results show that while the models provide some predictive power, they may not fully capture the complexity of the underlying relationships in the data. The improvement in performance from linear to ridge to random forest regression suggests that the data likely contains non-linear relationships. Although the
chosen analysis tools, (linear regression, ridge regression, and random forest regression) are appropriate for predicting a continuous target variable based on features, the results indicate that more sophisticated techniques might be necessary to capture the full complexity of the data, such as Deep Learning, neural networks, or further feature engineering.

The correlation between user ratings and average score aligns with the common intuition that higher ratings lead to greater success. The influence of involved companies on success and the relationship between genres and average score also seem plausible. The data provided a good starting point for analysis, but additional features such as marketing budget, release timing, and platform popularity could enhance predictive performance. Cleaning and restructuring the data, especially handling missing values and encoding categorical variables, were essential steps in preparing the dataset for analysis.
However, as seen in output.csv some fields such as companies involved have an ID rather than a company name. FOr example, instead of Sony we will have a number hard to interpret. This might make it a bit more difficult later on to interpret visually.  Overall, while the models provide some insight into factors influencing video game success, it is not fully accurate so further refinement, feature engineering, and potentially using more powerful models will improve the predictions. accuracy.




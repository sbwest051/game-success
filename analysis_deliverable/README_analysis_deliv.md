**ANALYSIS DELIVERABLE**

## Question 1

Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
**ML Component:**
We chose Linear Regression and Random Forest as our ML models and Ridge Regression to mitigate any overfitting.

**Linear Regression:** It's a more simple and effective technique suitable for predicting a continuous target variable (in this case, the average score of video games). It's a good starting point for understanding the linear relationship between features and the target variable.

**Random Forest:** Random forest regression is capable of capturing non-linear relationships between features and the target variable. It does this by constructing multiple decision trees and averaging their predictions, making it well-suited for complex datasets with non-linear patterns. It can also handle a large number of input variables and is robust to outliers and noisy data. It also automatically handles feature selection, reducing the need for extensive feature engineering.

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

## Questions 2 & 3:

What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

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
However, as seen in output.csv some fields such as companies involved have an ID rather than a company name. FOr example, instead of Sony we will have a number hard to interpret. This might make it a bit more difficult later on to interpret visually. Overall, while the models provide some insight into factors influencing video game success, it is not fully accurate so further refinement, feature engineering, and potentially using more powerful models will improve the predictions. accuracy.

**Hypothesis Component:**

### Two-sample t-test

**Objective**: Compare the means of two independent samples.
**Context**:
Average scores of games on multiple platforms versus single platforms.
Average scores of Shooter games versus non-Shooter games.
**Justification**: Determines if there are statistically significant differences between the group means under the assumption of unknown but equal variances.

**Hypothesis 1**: Games on Multiple Platforms vs. Single Platform

The hypothesis that we want to test is, on average, is the score of video games available on multiplayer vs single player? A two-sample t-test is used here, because it is designed to compare means from two independent groups. The predictor variable in this case is the multiplayer status of games, which determines whether test subjects can play a game together: ‘Multiple’ if yes (multiplayer greater than 0) and ‘Single’ if not (multiplayer of 0). Welch’s t-test is selected (welch=True) where variances of two groups for comparison are not required to be the same. Since different levels of exposure and market competition might have different impacts on the variance of games scores obtained on multiple platforms and a single platform, the assumption that the variance of these two groups is the same should be relaxed

Null Hypothesis: There is no difference in ratings between multiplayer and single-player games

Two-sample t-test Results:
T-statistic: -0.7399646416199741
P-value: 0.4596644633094552


**Hypthesis 2**:
For the second hypothesis, the aim is to test if Shooter games (represented by Genre1 value of 5) score higher on average than games from other genres. A two-sample t-test compared the average scores of games identified as Shooters with those that are not. This test is suitable as it provides a method to check if the mean scores are significantly different between the two categories, which are assumed to be independent of each other. This approach directly addresses the question of whether a specific genre, in this case, Shooters, is associated with higher or lower game scores compared to the broader market.

Null Hypothesis: There is no difference in ratings between shooter and non-shooter games

Two-sample t-test Results:
T-statistic: -0.3000267166266354
P-value: 0.7642949242767471

One-sample z-test for Shooter Games:
Z-score: 1.9292526396464995
P-value: 0.05369950613404994


**Hypothesis 3**:
This hypothesis explores whether games with a high number of reviews have different average scores compared to games with fewer reviews. The dataset is divided into two groups based on the median number of reviews: games with reviews greater than the median are categorized as 'high review' games, and those with reviews less than or equal to the median as 'low review' games. A two-sample t-test is used to compare the average scores between these two groups. This test is particularly relevant here as it checks for mean differences where independent groups are expected to exhibit potentially unequal variances, especially given the diverse nature of games and how review counts can reflect varying levels of user engagement and popularity.

Null Hypothesis: There is no difference in ratings between games with many reviews and games with few reviews.

Two-sample t-test for high vs. low review counts:
T-statistic: 6.5212444238160066
P-value: 1.1217226791417664e-10



### One-sample z-test

**Objective**: Compare the mean score of Shooter games against the overall mean score of all games.
**Justification**: Suitable for large datasets where the population standard deviation is known and the sample means are normally distributed.
Chi-squared TestFor examining associations between categorical variables.

## Data Preparation and Challenges

Handling missing values and ensuring data integrity.

Categorization of continuous data based on medians to define 'High' and 'Low' review counts.
Creation of indicators for distinguishing between multiple and single platform games.

### Hypotheses Testing Outcomes

**Multi vs. Single Platform Games**:
The p-value resulted at about 0.46, much above the 0.05 industry standard threshold for rejecting the null hypothesis.
This means that we currently accept the null hypothesis, which states that multplayer and single player games
have no significant difference in ratings.


**Shooter vs. Non-Shooter Games**:
The p-value came to about 0.764, even higher than the first tested hypothesis.
Similar to multiplayer vs. single-player games, this indicates the similarity between the distributions of shooter and
non-shooter games, and means we accept the null hypothesis, which states that shooter and non-shooter games
have no significant difference in ratings
**One-sample z-test for Shooter Games**:
Our p-value came to about 0.0537, very near the threshold of statistical significance. These results
confirm that the average scores of Shooter games are distinct from the overall average.
**NOTE**:There is a strange disparity between these solutions. Comparing shooter and non-shooter games directly suggests 
little difference between the populations, but calling a z-test on the shooter games with respect to the population
as a whole suggests a much larger difference. This leaves us with somewhat inconclusive results, but could possibly be explained by 
a higher variance in the distribution of shooter games, leading to discrepancies in the test, which assumes the same variance,
and showing a higher level of variation in the data.

 
**Number of Reviews to Score**:
The p value in this case was remarkably low: 1.12e-10. This means we must indelibly reject the null hypothesis:
our distributions of games with few reviews versus games with many reviews differ greatly. This suggests that in most
cases, people are more likely to leave reviews if they have positive comments for the game.

### Confidence and Reaction

## Further Insights

    If we had more time we would've liked to add additional datasets or cross-validation that could be used to strengthen the findings. If we could've incorporated data like user engagement or money made from the game it would've been a more helpful analysis

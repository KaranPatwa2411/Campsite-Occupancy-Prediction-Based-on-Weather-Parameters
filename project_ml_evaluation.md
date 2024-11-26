#### SER594: Machine Learning Evaluation  
#### Campsite Occupancy Prediction Based on Weather Parameters   
#### Karan Jignesh Patwa 
#### November 25, 2024

## Evaluation Metrics  

### Metric 1  
**Name:** Mean Squared Error (MSE)  

**Choice Justification:** MSE measures the average squared difference between predicted and actual values, giving more weight to large errors. It is suitable for this problem as it penalizes large deviations in occupancy predictions, which could significantly affect campsite resource planning.  

**Interpretation:** Lower MSE indicates better prediction accuracy.  

### Metric 2  
**Name:** R-squared (R²)  

**Choice Justification:** R² measures how well the regression predictions approximate the real data. It is appropriate for evaluating the goodness of fit of our regression models in predicting campsite occupancy trends.  

**Interpretation:** A value close to 1 indicates that the model explains most of the variance in the target variable.  

---

## Alternative Models  

### Alternative 1: Random Forest (Baseline)  
**Construction:** A Random Forest model was built as a baseline, using 100 estimators, a maximum depth of 15, and other tuned hyperparameters to balance accuracy and computational efficiency.  

**Evaluation:**  
- Mean Squared Error: **5,581,276.1757**  
- Mean Absolute Error: **687.7372**  
- R² Score: **0.9989**  

### Alternative 2: Ridge Regression  
**Construction:** Ridge Regression was implemented as an alternative to regularize the linear regression model, using an alpha value of 1.0 to penalize large coefficients and reduce overfitting.  

**Evaluation:**  
- Mean Squared Error: **144,544,936.8851**  
- Mean Absolute Error: **7,213.1884**  
- R² Score: **0.9714**  

### Alternative 3: Lasso Regression  
**Construction:** Lasso Regression was implemented to enforce sparsity in the model coefficients, using an alpha value of 0.01 to constrain model complexity.  

**Evaluation:**  
- Mean Squared Error: **144,535,227.2519**  
- Mean Absolute Error: **7,223.3878**  
- R² Score: **0.9714**  

---

## Best Model  

**Model:** Random Forest (Baseline)  


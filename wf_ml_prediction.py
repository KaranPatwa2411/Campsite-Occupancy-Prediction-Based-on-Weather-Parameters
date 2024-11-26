import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def prediction(X, y, model_file):
    
    with open(model_file, 'rb') as file:
        saved_data = pickle.load(file)
    
    
    pipeline = saved_data['pipeline']
    y_scaler = saved_data['scaler']

    
    if X is None:
        raise ValueError("Input X cannot be None")
    
    
    if not isinstance(X, pd.DataFrame):
        try:
            
            column_names = pipeline.named_steps['preprocessor'].get_feature_names_out()
            X = pd.DataFrame(X, columns=column_names)
        except:
            
            X = pd.DataFrame(X)

    
    if y is None:
        raise ValueError("Input y cannot be None")
    
    
    if isinstance(y, pd.Series):
        y = y.values
    
    
    y_pred_normalized = pipeline.predict(X)

    
    y_pred = y_scaler.inverse_transform(y_pred_normalized.reshape(-1, 1)).flatten()

    
    y_actual = y.flatten()

    
    mse = mean_squared_error(y_actual, y_pred)
    mae= mean_absolute_error(y_actual, y_pred)
    r2 = r2_score(y_actual, y_pred)

    
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

    
    comparison = pd.DataFrame({
        'Actual': y_actual, 
        'Predicted': y_pred
    })
    print(comparison.head())

    return mse, mae, r2
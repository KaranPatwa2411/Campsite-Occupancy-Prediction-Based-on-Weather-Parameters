import os
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from wf_ml_training import wf_ml_training
from wf_ml_prediction import prediction

def wf_ml_evaluation(data_file, model_file, evaluation_file):
    
    df = pd.read_csv(data_file)
    target_col = 'arrivals_count'
    X = df.drop(columns=['date', target_col], errors='ignore')
    y = df[target_col]
    
    
    with open(model_file, 'rb') as file:
        model_data = pickle.load(file)
        pipeline = model_data['pipeline']  
        scaler = model_data['scaler']      
    
    
    preprocessor = pipeline.named_steps['preprocessor']
    X_preprocessed = preprocessor.transform(X)
    
    
    models = {
        'Random Forest (Baseline)': RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ),
        'Ridge Regression': Ridge(alpha=1.0),
        'Lasso Regression': Lasso(alpha=0.01),
    }
    evaluation_results = []
    
    os.makedirs('models', exist_ok=True)
    
    for model_name, model in models.items():
        
        model.fit(X_preprocessed, y)
        y_pred = model.predict(X_preprocessed)
        
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        
        evaluation_results.append(
            f"{model_name}:\n"
            f"  Mean Squared Error: {mse:.4f}\n"
            f"  Mean Absolute Error: {mae:.4f}\n"
            f"  R2 Score: {r2:.4f}\n"
        )
        
        model_save_path = os.path.join('models', f'{model_name.replace(" ", "_").lower()}.pkl')
        with open(model_save_path, 'wb') as file:
            pickle.dump({
                'model': model,
                'mse': mse,
                'mae': mae,
                'r2': r2
            }, file)
        print(f"Saved {model_name} to {model_save_path}")
    
    
    os.makedirs(os.path.dirname(evaluation_file), exist_ok=True)
    
    mse,mae,r2= prediction(X_test, y_test, model_file) 
    evaluation_results.append(
            f"Random Forest Main model:\n"
            f"  Mean Squared Error: {mse:.4f}\n"
            f"  Mean Absolute Error: {mae:.4f}\n"
            f"  R2 Score: {r2:.4f}\n"
        )
    with open(evaluation_file, 'w') as file:
        file.writelines(evaluation_results)
    print(f"Evaluation summary saved to {evaluation_file}")


data_file = r'data_processing\processed_data.csv'
model_file = 'models/random_forest_model.pkl'
evaluation_file = 'evaluation/summary.txt'

df = pd.read_csv(data_file)
df = df.sort_values(by='date')  

target_col = 'arrivals_count'
X = df.drop(columns=['date', target_col], errors='ignore')
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.to_csv('data_processing/X_train.csv', index=False)
X_test.to_csv('data_processing/X_test.csv', index=False)
y_train.to_csv('data_processing/y_train.csv', index=False)
y_test.to_csv('data_processing/y_test.csv', index=False)

wf_ml_training(df, model_file)  
wf_ml_evaluation(data_file, model_file, evaluation_file)
 
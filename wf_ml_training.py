import os
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def wf_ml_training(df, model_file):
    
    df=df
        
    df = df.sort_values(by='date')

    target_col = 'arrivals_count'
    features = df.drop(columns=['date', target_col], errors='ignore')
    target = df[target_col]

    
    numerical_cols = features.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_cols = features.select_dtypes(include=['object']).columns.tolist()

    
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  
        ('scaler', StandardScaler())  
    ])
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    
    scaler = MinMaxScaler()
    target_normalized = scaler.fit_transform(target.values.reshape(-1, 1))

    
    X_train, X_test, y_train, y_test = train_test_split(features, target_normalized, test_size=0.2, random_state=42)

    
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    
    pipeline.fit(X_train, y_train.ravel())

    
    os.makedirs(os.path.dirname(model_file), exist_ok=True)
    with open(model_file, 'wb') as file:
        pickle.dump({'pipeline': pipeline, 'scaler': scaler}, file)

    print(f"Model saved to {model_file}")

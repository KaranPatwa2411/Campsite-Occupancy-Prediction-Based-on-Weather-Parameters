import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visuals():
    df= pd.read_csv('./data_processing/processed_data.csv')

    quantitative_features = ['arrivals_count','vacation_pitches_count','vacation_pitches_open','mean_frost_depth','std_drought_index']
    qualitative_feature = 'land'

    quant_summary = df[quantitative_features].agg(['min', 'max', 'median'])

    qual_summary = {
        'Number of Categories': df[qualitative_feature].nunique(),
        'Most Frequent': df[qualitative_feature].value_counts().nlargest(1).to_dict(),
        'Least Frequent': df[qualitative_feature].value_counts().nsmallest(1).to_dict()
    }

    with open('data_processed/summary.txt', 'w') as f:
        f.write("Quantitative Summary:\n")
        f.write(quant_summary.to_string())
        f.write("\n\nQualitative Summary:\n")
        for key, value in qual_summary.items():
            f.write(f"{key}: {value}\n")

    correlation_matrix = df[quantitative_features].corr()


    lower_triangle = correlation_matrix.where(np.tril(np.ones(correlation_matrix.shape)).astype(bool))

    with open('data_processed/correlations.txt', 'w') as f:
        f.write("Correlation Matrix:\n")
        f.write(lower_triangle.to_string())

    for i in range(len(quantitative_features)):
        for j in range(i + 1, len(quantitative_features)):
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=df, x=quantitative_features[i], y=quantitative_features[j])
            plt.title(f'Scatter Plot: {quantitative_features[i]} vs {quantitative_features[j]}')
            plt.xlabel(quantitative_features[i])
            plt.ylabel(quantitative_features[j])
            plt.grid(True)
            plt.savefig(f'visuals/scatter_{quantitative_features[i]}_{quantitative_features[j]}.png')
            plt.close()


    plt.figure(figsize=(15, 10))
    sns.countplot(data=df, x=qualitative_feature, order=df[qualitative_feature].value_counts().index)
    plt.title(f'Histogram of {qualitative_feature}')
    plt.xlabel(qualitative_feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.savefig(f'visuals/histogram_{qualitative_feature}.png')
    plt.close()


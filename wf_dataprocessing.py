import pandas as pd
import os

def processing():
    df = pd.read_csv(r'./data_original/weather_and_campsite_data.csv')
    df.head()
    print(df.columns)
    """as it can be seen some column names are in German so I will translated them into english and made changes here
    for better understanding"""
    df = df.rename(columns={
        'anteil_urlaubs_stellplaetze_offen_an_urlaubs_stellplaetze_anzahl': 'proportion_of_open_vacation_pitches',
        'ankuenfte_anzahl': 'arrivals_count',
        'ankuenfte_veraenderung_zum_vorjahreszeitraum_prozent': 'arrivals_change_from_previous_year_percent',
        'uebernachtungen_anzahl': 'overnight_stays_count',
        'uebernachtungen_veraenderung_zum_vorjahreszeitraum_prozent': 'overnight_stays_change_from_previous_year_percent',
        'durchsch_aufenthaltsdauer_tage': 'average_stay_duration_days',
        'campingplaetze_anzahl': 'campgrounds_count',
        'urlaubs_campingplaetze_anzahl': 'vacation_campgrounds_count',
        'urlaubs_campingplaetze_offen': 'vacation_campgrounds_open',
        'urlaubs_stellplaetze_anzahl': 'vacation_pitches_count',
        'urlaubs_stellplaetze_offen': 'vacation_pitches_open',
        'change_urlaubs_stellplaetze_offen_vorjahresmonat': 'change_vacation_pitches_open_previous_month'
    })

    print(df.columns)
    df.info()#to show how many empty values exist now I will perform some data preprocessing methods to fill these values because dropping them does not make sense
    df_copy=df.copy()#just for backup if anything goes wrong in df during preprocessing
    df['arrivals_count'] = df['arrivals_count'].fillna(df.groupby('land')['arrivals_count'].transform('mean'))
    df['overnight_stays_count'] = df['overnight_stays_count'].fillna(df.groupby('land')['overnight_stays_count'].transform('mean'))
    df['previous_year_arrivals'] = df.groupby('land')['arrivals_count'].shift(1)
    #calculated percentage for the mentioned column
    df['arrivals_change_from_previous_year_percent'] = (
        (df['arrivals_count'] - df['previous_year_arrivals']) / df['previous_year_arrivals'] * 100
    )

    df.drop(columns=['previous_year_arrivals'], inplace=True)

    df['previous_year_overnight_stays'] = df.groupby('land')['overnight_stays_count'].shift(1)
    df['overnight_stays_change_from_previous_year_percent'] = (
        (df['overnight_stays_count'] - df['previous_year_overnight_stays']) / df['previous_year_overnight_stays'] * 100
    )
    df.drop(columns=['previous_year_overnight_stays'], inplace=True)

    df['average_stay_duration_days'] = df['average_stay_duration_days'].fillna(
        df.groupby('land')['average_stay_duration_days'].transform('mean')
    )

    df['campgrounds_count'] = df['campgrounds_count'].fillna(df.groupby('land')['campgrounds_count'].transform('mean'))

    df['vacation_campgrounds_count'] = df.groupby('land')['vacation_campgrounds_open'].transform(lambda group: group.interpolate(method='linear').ffill().bfill())

    df['vacation_campgrounds_open'] = df.groupby('land')['vacation_campgrounds_open'].transform(lambda group: group.interpolate(method='linear').ffill().bfill())

    df['vacation_pitches_count'] = df['vacation_pitches_count'].fillna(
        df.groupby('land')['vacation_pitches_count'].transform('mean')
    )

    df['vacation_pitches_open'] = df.groupby('land')['vacation_campgrounds_open'].transform(lambda group: group.interpolate(method='linear').ffill().bfill())

    df['change_vacation_pitches_open_previous_month'] = df['change_vacation_pitches_open_previous_month'].interpolate(method='linear')

    df['calculated_proportion'] = df['vacation_pitches_open'] / df['vacation_pitches_count']
    df['proportion_of_open_vacation_pitches'].fillna(df['calculated_proportion'], inplace=True)
    df.drop(columns=['calculated_proportion'], inplace=True)

    df.info()

    df.dropna()
    df.info()
    df.to_csv('./data_processing/processed_data.csv', index=False)
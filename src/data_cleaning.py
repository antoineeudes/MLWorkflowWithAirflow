import pandas as pd
import os

TRAINING_FILE_PATH = os.path.join(os.environ.get('AIRFLOW', 'data/cs-training.csv'))

def clean_data():
    dataframe = pd.read_csv(TRAINING_FILE_PATH).drop('Unnamed: 0', axis = 1)

    dataframe.loc[
        dataframe["NumberOfTime30-59DaysPastDueNotWorse"] > 20,
        'NumberOfTime30-59DaysPastDueNotWorse',
    ] = dataframe["NumberOfTime30-59DaysPastDueNotWorse"].median()

    dataframe.loc[
        dataframe.NumberOfTimes90DaysLate > 20,
        'NumberOfTimes90DaysLate',
    ] = dataframe.NumberOfTimes90DaysLate.median()

    dataframe.loc[
        dataframe.NumberOfDependents.isnull(),
        'NumberOfDependents',
    ] = dataframe.NumberOfDependents.median()

    dataframe.loc[
        dataframe.NumberOfDependents > 10,
        'NumberOfDependents',
    ] = 10

    dataframe.loc[
        dataframe.RevolvingUtilizationOfUnsecuredLines > 5,
        'RevolvingUtilizationOfUnsecuredLines',
    ] = dataframe.RevolvingUtilizationOfUnsecuredLines.median()

    dataframe.loc[
        dataframe.DebtRatio > 1,
        'DebtRatio',
    ] = dataframe.DebtRatio.median()


    dataframe.loc[dataframe.MonthlyIncome.isnull(), 'MonthlyIncome'] = dataframe.MonthlyIncome.median()

    dataframe.loc[
        dataframe["NumberOfTime60-89DaysPastDueNotWorse"] > 20,
        "NumberOfTime60-89DaysPastDueNotWorse",
    ] = dataframe["NumberOfTime60-89DaysPastDueNotWorse"].median()

    dataframe.to_csv(TRAINING_FILE_PATH)

import pandas as pd
from utils import get_training_dataframe, save_training_dataframe_to_csv

def clean_data():
    dataframe = get_training_dataframe()

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

    save_training_dataframe_to_csv(dataframe)

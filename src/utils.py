import pandas as pd
import pickle
import os

TRAINING_FILE_PATH = os.path.join(os.environ.get('AIRFLOW', 'data/cs-training.csv'))
ESTIMATOR_PATH = os.path.join(os.environ.get('AIRFLOW_HOME'), 'estimator.pickle')

def get_training_dataframe():
    return pd.read_csv(TRAINING_FILE_PATH).drop('Unnamed: 0', axis = 1)

def save_training_dataframe_to_csv(dataframe):
    dataframe.to_csv(TRAINING_FILE_PATH)

def save_estimator(estimator):
    pickle.dump(estimator, open(ESTIMATOR_PATH, 'wb'))
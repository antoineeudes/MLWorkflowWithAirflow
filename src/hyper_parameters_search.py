from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from utils import get_cleaned_training_dataframe

def hyper_parameters_search(parameters, **kwargs):
    dataframe = get_cleaned_training_dataframe()
    X = dataframe.drop('SeriousDlqin2yrs', axis=1)
    y = dataframe.SeriousDlqin2yrs

    gs = GridSearchCV(GradientBoostingClassifier(), parameters, scoring='roc_auc')
    gs.fit(X, y)
 
    return gs
import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict):
    try:
        report = {}

        for model_name, model in models.items():
            param_grid = params.get(model_name, {})  # safely get params

            if param_grid:  # run GridSearch if params available
                gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)
                gs.fit(X_train, y_train)
                model.set_params(**gs.best_params_)
            
            # fit final model
            model.fit(X_train, y_train)

            # predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            # log both train & test scores
            report[model_name] = {
                "train_score": train_score,
                "test_score": test_score
            }

        return report

    except Exception as e:
        raise CustomException(e, sys)

    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

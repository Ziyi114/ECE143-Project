# Define Machine Learning Models
from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()
from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()
from sklearn import svm
model_SVR = svm.SVR()
from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()
from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor()
from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor()
from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor()
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()


def get_models():
    """
    :return: a list of all the machine learning models
    """
    models = [model_DecisionTreeRegressor, model_LinearRegression, model_SVR, model_KNeighborsRegressor,
              model_RandomForestRegressor, model_AdaBoostRegressor, model_GradientBoostingRegressor,
              model_BaggingRegressor, model_ExtraTreeRegressor]
    return models

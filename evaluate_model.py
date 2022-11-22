from sklearn.model_selection import cross_val_score


def evaluate_model(model, X, y):
    """
    This function runs 5-fold cross validation
    :param model: ML model
    :param X: list, features set
    :param y: list, labels
    :return: the best performance score from 5-fold cross validation
    """
    scores = cross_val_score(model, X, y, cv=5, n_jobs=-1)
    return scores.max()

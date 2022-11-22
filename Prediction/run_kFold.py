import get_models
import evaluate_model


def run_kFold(X, y):
    """
    This function runs 5-fold cross validation on all machine learning
    models we selected
    :param X: list, features set
    :param y: list, labels
    :return: performance of all models
    """
    scores = []
    models = get_models.get_models()
    for model in models:
        scores.append(evaluate_model.evaluate_model(model, X, y))
    return scores

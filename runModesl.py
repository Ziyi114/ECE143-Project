import get_models
import try_different_method


def runModel(X, y):
    """
    This function runs and evaluates all the models' performance
    :param X:
    :param y:
    :return: scores of all the models
    """
    scores = []
    models = get_models.get_models()
    for model in models:
        acc = try_different_method.try_different_method(X, y, model, str(model))
        scores.append(acc)
    return scores

import get_set
import matplotlib.pyplot as plt
import numpy as np


def try_different_method(X, y, model, model_name):
    """
    this function is to experiment on diffrent models display their performance

    :param X: list, features set
    :param y: list, labels
    :param model: model for predicting
    :param model_name: name of the model
    :rtype: float
    """
    assert isinstance(X, list)
    assert isinstance(y, list)
    assert isinstance(model_name, str)
    X_train, X_test, y_train, y_test = get_set.get_set(X, y)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    result = model.predict(X_test)
    plt.figure()
    plt.plot(np.arange(len(result)), y_test, 'go-', label='true value')
    plt.plot(np.arange(len(result)), result, 'ro-', label='predict value')
    plt.title(model_name + '\n' + 'score: %f' % score)
    plt.legend()
    plt.show()
    return score

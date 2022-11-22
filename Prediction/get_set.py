from sklearn.model_selection import train_test_split


def get_set(X, y):
    """
    this function is to divide our X and y into trainning and testing sets

    :param X: list, features set
    :param y: list, labels
    :rtype: tuple
    """
    assert isinstance(X, list)
    assert isinstance(y, list)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

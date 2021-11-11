from numpy import sqrt, dot


def euclidian_norm(x):
    """

    :param x: It's a colum vector
    :return:
    """

    return sqrt(dot(x.t, x))

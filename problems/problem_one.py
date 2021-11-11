from numpy import exp, zeros


class problem:
    def __init__(self):
        pass

    def cost_function(self, x):
        """
        :param x: it's a vector or a list
        :return:
        """

        x_1 = x[0]
        x_2 = x[1]

        return exp(x_1 + 3 * x_2 - 0.1) + exp(x_1 - 2 * x_2 - 0.1) + exp(-x_1 - 0.2)

    def gradient(self, x):
        """
            This function has a input that belongs to R^2, so the gradient will be a vector of shape (1x2)
        :param x:
        :return:
        """
        gradient_vector = zeros((2, 1))

        x_1 = x[0]
        x_2 = x[1]

        gradient_vector[0] = exp(x_1 + 3 * x_2 - 0.1) + exp(x_1 - 2 * x_2 - 0.1) - exp(-x_1 - 0.2)
        gradient_vector[1] = exp(x_1 + 3 * x_2 - 0.1) + exp(x_1 - 2 * x_2 - 0.1)

        return gradient_vector

    def hessian(self, x):
        """
              This function has a input that belongs to R^2, so the hessian will be a matrix of shape (2x2)
        :param x:
        :return:
        """
        hessian_matrix = zeros((2, 2))

        x_1 = x[0]
        x_2 = x[1]

        hessian_matrix[0][0] = self.cost_function(x)
        hessian_matrix[0][1] = 3*exp(x_1 + 3 * x_2 - 0.1) - 2 * exp(x_1 - 2 * x_2 - 0.1)
        hessian_matrix[1][0] = hessian_matrix[0][1]
        hessian_matrix[1][1] = 6*exp(x_1 + 3 * x_2 - 0.1) + 4 * exp(x_1 - 2 * x_2 - 0.1)

        return hessian_matrix

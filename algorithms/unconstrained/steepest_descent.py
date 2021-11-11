from numpy import det, matrix
from numpy.linalg import inv
from algorithms.unconstrained.descent_method import descent


class steepestDescent(descent):

    def __init__(self, cost_function: function, P: matrix , norm='quadratic'):
        super().__init__(cost_function)

        if det(P) == 0:
            print("Matrix P do not have an inverse, try an non-singular matrix")

        self.P = P
        self.norm = norm

    def update(self, *args):
        if not self._stop_criterium(gradient, x):
            self._calculate_descent_direction(gradient, x)
            self._calculate_step_size(gradient, x)

            x += self.step_size * self.descent_direction

    def _calculate_descent_direction(self, gradient: function, x):
        if self.norm == 'quadratic':
            self.descent_direction = -inv(self.P)*gradient(x)

    def _stop_criterium(self, gradient: function, x):
        """
        :param gradient:
        :param x:
        :return:
        """
        return euclidian_norm(gradient(x)) <= self.epsilum

    def _calculate_step_size(self, x):

        if self.step_size_method == 'line_search':
            super()._line_search(x),
        if self.step_size_method == 'backtracking':
            super()._backtracking(x, gradient, self.alpha, self.beta)
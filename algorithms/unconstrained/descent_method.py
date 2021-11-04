from numpy import dot, arange, argmin


class descent:
    def __init__(self, cost_function: function, method='gradient', step_size_method='line'):
        """

        :param cost_function:
        :param method:
        :param step_size_method:
        """
        self.method = method
        self.step_size_method = step_size_method
        self.cost_function = cost_function

    def update(self, x):
        x = x + self.step_size_method*self.descent_direction

    def _calculate_new_step_size(self, *args):
        methods = {
            'line': self._line_search,
            'backtracking': self._backtracking
        }

        methods[self.step_size_method](args)

    def _calculate_descent_direction(self, *args):
        methods = {
            'gradient': self._gradient_descent,
            'steepest': self._steepest_descent,
            'newton': self._newton
        }

        methods[self.method](args)



    def _gradient_descent(self, gradient):
        return -gradient

    def _steepest_descent(self):
        pass

    def _newton(self):
        pass

    def _line_search(self, x):
        """

        :param x:
        :return:
        """
        output = self.cost_function(x + self.step_size*self.descent_direction) + 1e-10
        indice = argmin(output)

        self.step_size = output[indice]

    def _backtracking(self, x, gradient=None, alpha=None, beta=None):
        """
        :param x:
        :param gradient:
        :param alpha: α ∈ (0, 1/2)
        :param beta: β ∈ (0, 1)
        :return:
        """
        part_one = self.cost_function(x + self.step_size*self.descent_direction)
        part_two = self.cost_function(x) + alpha*self.step_size*dot(gradient.T, self.step_size)

        if part_one >= part_two:
            self.step_size = beta*self.step_size


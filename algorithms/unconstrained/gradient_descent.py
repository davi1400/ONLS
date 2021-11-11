from algorithms.unconstrained.descent_method import descent


class gradientDescent(descent):

    def __init__(self, cost_function: function,  step_size_method='line_search', alpha=None, beta=None):
        """

        :param cost_function:
        :param step_size_method:
        :param alpha:
        :param beta:
        """
        super().__init__(cost_function)

        self.alpha = alpha
        self.beta = beta
        self.step_size = super().step_size
        self.step_size_method = step_size_method

    def update(self, gradient: function, x):
        """

        :param gradient:
        :param x:
        :return:
        """
        if not self._stop_criterium(gradient, x):
            self._calculate_descent_direction(gradient, x)
            self._calculate_step_size(gradient, x)

            x += self.step_size * self.descent_direction


    def _calculate_descent_direction(self, gradient: function, x):
        """

        :param gradient:
        :param x:
        :return:
        """
        self.descent_direction = -gradient(x)

    def _stop_criterium(self, gradient: function, x):
        """

        :param gradient:
        :param x:
        :return:
        """
        return euclidian_norm(gradient(x)) <= self.epsilum

    def _calculate_step_size(self, gradient: function, x):
        """

        :param gradient:
        :param x:
        :return:
        """
        if self.step_size_method == 'line_search':
            super()._line_search(x),
        if self.step_size_method == 'backtracking':
            super()._backtracking(x, gradient, self.alpha, self.beta)

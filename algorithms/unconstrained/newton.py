from numpy import dot
from numpy.linalg import inv
from algorithms.unconstrained.descent_method import descent


class newton(descent):
    def __init__(self, cost_function: function):
        super().__init__(cost_function)

    def update(self, hessian: function, gradient: function, x):
        if not self._stop_criterium(hessian, gradient, x):
            self._calculate_descent_direction(hessian, gradient, x)
            self._calculate_step_size(gradient, x)

            x += self.step_size * self.descent_direction

    def _calculate_descent_direction(self, hessian: function, gradient: function, x):
        self.descent_direction = -inv(hessian(x)) * gradient(x)

    def _stop_criterium(self, hessian: function, gradient: function, x):
        lamba = dot(gradient(x).T, dot(inv(hessian(x)), gradient(x)))

        return lamba / 2 <= self.epsilum

    def _calculate_step_size(self):
        pass

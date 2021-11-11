from numpy import dot, arange, argmin
from utils import euclidian_norm
from abc import abstractmethod


class descent:
    def __init__(self, cost_function: function, epsilum=1e-10):
        """

        :param cost_function:
        :param method:
        :param step_size_method:
        """

        self.step_size = None
        self.epsilum = epsilum
        self.cost_function = cost_function


    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def _calculate_descent_direction(self, *args):
        pass

    @abstractmethod
    def _stop_criterium(self, *agrs):
        pass


    def _line_search(self, x):
        """

        :param x:
        :return:
        """
        output = self.cost_function(x + self.step_size * self.descent_direction) + 1e-10
        indice = argmin(output)

        self.step_size = output[indice]

    def _backtracking(self, x, gradient: function, alpha=None, beta=None):
        """
        :param x:
        :param gradient:
        :param alpha: α ∈ (0, 1/2)
        :param beta: β ∈ (0, 1)
        :return:
        """
        part_one = self.cost_function(x + self.step_size * self.descent_direction)
        part_two = self.cost_function(x) + alpha * self.step_size * dot(gradient(x).T, self.step_size)

        if part_one >= part_two:
            self.step_size = beta * self.step_size
        else:
            re

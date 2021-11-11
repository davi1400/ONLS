import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


class levelCurves:
    def __init__(self, cost_func):
        self.cost_func = cost_func


    def plot(self, x):
        N, M = x.shape

        # we have M dimensions, if M is greater than three we cant plot it.
        if M > 2:
            return
        else:
            if M == 2:
                x1 = x[:, 0]
                x2 = x[:, 1]

            x_mesh, y_mesh = np.meshgrid(x1, x2)
            z = self.cost_func(x)

            fig, ax = plt.subplots(figsize=(10, 10))
            CS = ax.contour(x_mesh, y_mesh, z, 20, colors='k')
            ax.clabel(CS, inline=0.5, fontsize=10)
            ax.set_title('Curvas de nivel')
            plt.show()







if __name__ == '__main__':


    delta = 0.1
    alpha = 10

    x1 = []
    x2 = []

    x1 = np.arange(-5, 5, 0.1)
    x2 = np.arange(-5, 5, 0.1)

    x, y = np.meshgrid(x1, x2)

    z = x**2 + y**2
    # z = -x**2 - 2*y**2 - 1

    fig, ax = plt.subplots(figsize=(10, 10))
    CS = ax.contour(x, y, z, 20, cmap='viridis')
    ax.clabel(CS, inline=0.5, fontsize=10)
    ax.set_title('Curvas de nivel')
    plt.show()

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # plotting a scatter for example
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
    plt.show()
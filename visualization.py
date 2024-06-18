import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_toolpath(toolpath,):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs, ys, zs = zip(*toolpath)
    ax.plot(xs, ys, zs)
    plt.show()
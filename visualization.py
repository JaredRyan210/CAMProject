import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_toolpath(toolpath, title="Toolpath Visualization"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs, ys, zs = zip(*toolpath)

    ax.plot(xs, ys, zs, label='ToolPath')

    ax.scatter(xs[0], ys[0], zs[0], color='green', s=100, label='Start', marker='o')
    
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=100, label='End', marker='x')

    ax.set_title(title)
    ax.legend()

    plt.show()
    
    
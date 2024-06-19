import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh

def visualize_toolpath_with_model(model, toolpath, title="Toolpath Visualization"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    '''
    
    
    for vector in model.vectors:
        ax.plot([vector[0][0], vector[1][0]], [vector[0][1], vector[1][1]], [vector[0][2], vector[1][2]], color='gray')
        ax.plot([vector[1][0], vector[2][0]], [vector[1][1], vector[2][1]], [vector[1][2], vector[2][2]], color='gray')
        ax.plot([vector[2][0], vector[0][0]], [vector[2][1], vector[0][1]], [vector[2][2], vector[0][2]], color='gray')
    '''

    xs, ys, zs = zip(*toolpath)

    ax.plot(xs, ys, zs, label='ToolPath', color='blue')

    ax.scatter(xs[0], ys[0], zs[0], color='green', s=100, label='Start', marker='o')
    
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=100, label='End', marker='x')

    ax.set_title(title)
    ax.legend()

    plt.show()
    
    
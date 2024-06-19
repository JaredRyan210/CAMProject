import numpy as np

def generate_toolpath(model):
    toolpath = []
    # Example of simple linear path
    for point in model.vectors:
        toolpath.append((point[0][0], point[0][1], point[0][2]))
    return toolpath

def generate_contour_toolpath(model):
    toolpath = []
    z_levels = np.unique(model.vectors[:, 2])
    for z in z_levels:
        layer_points = model.vectors[model.vectors[:, 2] == z]
        for point in layer_points:
            toolpath.append((point[0], point[1], z))
    return toolpath

def generate_raster_toolpath(model, step_over=0.1):
    toolpath = []
    min_y = np.min(model.vectors[:, 1])
    max_y = np.max(model.vectors[:, 1])
    y_steps = np.arange(min_y, max_y, step_over)
    
    for y in y_steps:
        layer_points = model.vectors[model.vectors[:, 1] == y]
        for point in layer_points:
            toolpath.append((point[0], y, point[2]))
    return toolpath
    
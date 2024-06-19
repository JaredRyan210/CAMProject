import numpy as np

def generate_linear_toolpath(model):
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

def generate_pocketing_toolpath(model, step_over=0.1):
    toolpath = []
    min_z = np.min(model.v0[:, 2])
    max_z = np.max(model.v0[:, 2])
    z_steps = np.arange(min_z, max_z, step_over)
    
    for z in z_steps:
        layer_points = model.v0[model.v0[:, 2] == z]
        for point in layer_points:
            toolpath.append((point[0], point[1], z))
    return toolpath

def generate_helical_toolpath(center, radius, pitch, height):
    toolpath = []
    z = center[2]
    angle = 0
    while z <= center[2] + height:
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        toolpath.append((x, y, z))
        angle += pitch
        z += pitch / (2 * np.pi)  # Increment z by the pitch divided by 2*pi to create the helix
    return toolpath

def generate_pyramid_toolpath(model, layer_height=1.0, step_over=0.5):
    toolpath = []
    
    # Find the min and max Z values to determine the height of the pyramid
    min_z = np.min(model.vectors[:, 2])
    max_z = np.max(model.vectors[:, 2])
    
    # Step through the layers from the base to the apex
    z_levels = np.arange(min_z, max_z + layer_height, layer_height)
    
    for z in z_levels:
        layer_points = []
        for vector in model.vectors:
            if np.all(vector[:, 2] <= z):
                for point in vector:
                    if point[2] <= z:
                        layer_points.append(point)
        
        if len(layer_points) > 0:
            # Sort points for a continuous path (optional, depends on specific requirements)
            layer_points = np.array(layer_points)
            layer_points = layer_points[layer_points[:, 0].argsort()]  # Sort by X coordinate
            
            for point in layer_points:
                toolpath.append((point[0], point[1], z))
    
    return toolpath


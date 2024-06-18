

def generate_toolpath(model):
    toolpath = []
    # Example of simple linear path
    for point in model.vectors:
        toolpath.append((point[0][0], point[0][1], point[0][2]))
    return toolpath
    


def toolpath_to_gcode(toolpath):
    gcode = []
    for point in toolpath:
        gcode.append(f"G1 X{point[0]} Y{point[1]} Z{point[2]}")
    return gcode
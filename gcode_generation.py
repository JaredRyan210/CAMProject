

def toolpath_to_gcode(toolpath):
    gcode = []
    for point in toolpath:
        gcode.append(f"G1 X{point[0]} Y{point[1]} Z{point[2]}")
    return gcode

def generate_gcode(toolpath, feed_rate=1500, spindle_speed=12000):
    gcode = []

    gcode.append("G21 ; Set units to millimeters")
    gcode.append("G17 ; Select XY Plane")
    gcode.append(f"G90 ; Absolute Positioning")
    gcode.append(f"M3 S{spindle_speed} ; Start spindle at {spindle_speed} RPM")

    start_point = toolpath[0]
    gcode.append(f"G0 X{start_point[0]:.3f} Y{start_point[1]:.3f} Z{start_point[2]:.3f}")

    for point in toolpath:
        gcode.append(f"G1 X{point[0]:.3f} Y{point[1]:.3f} Z{point[2]:.3f} F{feed_rate}")

    gcode.append("M5 ; Stop Spindle")
    gcode.append("G0 Z10 ; Raise Z axis")
    gcode.append("G0 X0 Y0 ; Return to home position")
    gcode.append("M30 ; End of program")

    return gcode

def save_gcode(file_path, gcode):
    with open(file_path, 'w') as file:
        for line in gcode:
            file.write(line + '\n')
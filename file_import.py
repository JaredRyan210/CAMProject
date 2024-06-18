import numpy as np
from stl import mesh

def load_stl(file_path):
    model = mesh.Mesh.from_file(file_path)
    return model
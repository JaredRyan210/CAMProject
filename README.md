# CAMProject

CAMProject is a computer-Aided Manufacturing (CAM) software developed to generate toolpaths and corresponding G-code for 3D models (.stl).

## Fucntionality

The software includes functionalities for loading STL files, generating different types of toolpaths, visualizing them, and exporting G-code for CNC machining

## Features

- Load and visualize STL files
- Generate various types of toolpaths:
    - Linear
    - Contour
    - Raster
    - Pocketing
    - Helical
    - Pyramid
- Visualize toolpaths with the model
- Export generated toolpaths to G-code

## Installation

To run, install the required dependencies with command:

pip install -r requirements.txt

## Usage

To run the application, run the 'main.py' script:

python main.py

## GUI Overview

The application provides a graphical user interface (GUI) with the following components:

- **Toolpath Type Selector**: Choose the type of toolpath to generate.

- **Open File Button**: Load an STL file for toolpath generation.

- **Generate G-code Button**: Generate and save the G-code from the generated toolpath.

## Main Files

- **'main.py'**: Initializes and starts GUI.

- **'file_import.p'**: Handles loading STL files.

- **'gcode_generation.py'**: Conatains functions to generate and save G-code.

- **'toolpath_generation'**: Provides functions to generate different types of toolpaths.

- **'visualization.py'**: Contains functions to visualize the model and the generated toolpath.

- **'gui.py'**: Implements the GUI using PyQt5.


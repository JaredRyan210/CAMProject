import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QComboBox, QVBoxLayout, QWidget
from file_import import load_stl
from toolpath_generation import *
from visualization import visualize_toolpath_with_model
from gcode_generation import generate_gcode, save_gcode

class CAMSoftware(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing UI")
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('CAM Software')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.toolpathComboBox = QComboBox(self)
        self.toolpathComboBox.addItems(["Linear", "Contour", "Raster", "Pocketing", "Helical", "Pyramid"])
        layout.addWidget(self.toolpathComboBox)

        self.openButton = QPushButton('Open File', self)
        self.openButton.clicked.connect(self.open_file)
        layout.addWidget(self.openButton)

        self.generateGcodeButton = QPushButton('Generate G-code', self)
        self.generateGcodeButton.clicked.connect(self.generate_gcode)
        layout.addWidget(self.generateGcodeButton)

        central_widget.setLayout(layout)
        print("UI Initialized")

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)", options=options)
        if file_path:
            model = load_stl(file_path)
            toolpath_type = self.toolpathComboBox.currentText()
            if toolpath_type == 'Linear':
                self.toolpath = generate_linear_toolpath(model)
            elif toolpath_type == "Contour":
                self.toolpath = generate_contour_toolpath(model)
            elif toolpath_type == "Raster":
                self.toolpath = generate_raster_toolpath(model)
            elif toolpath_type == "Pocketing":
                self.toolpath = generate_pocketing_toolpath(model)
            elif toolpath_type == "Helical":
                self.toolpath = generate_helical_toolpath((0,0,0), 10, 0.5, 50)
            elif toolpath_type == "Pyramid":
                self.toolpath = generate_pyramid_toolpath(model)

            visualize_toolpath_with_model(model, self.toolpath, f"{toolpath_type} Toolpath")

    def generate_gcode(self):
        if hasattr(self, 'toolpath'):
            gcode = generate_gcode(self.toolpath)
            save_path, _ = QFileDialog.getSaveFileName(self, "Save G-code File", "", "G-code Files (*.gcode);;All Files (*)")
            if save_path:
                save_gcode(save_path, gcode)
                print(f"G-code saved to: {save_path}")
        else:
            print("No toolpath generated")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cam_software = CAMSoftware()
    cam_software.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QComboBox, QVBoxLayout, QWidget
from file_import import load_stl
from toolpath_generation import *
from visualization import visualize_toolpath_with_model

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
        self.toolpathComboBox.addItems(["Contour", "Raster", "Pocketing", "Helical"])
        layout.addWidget(self.toolpathComboBox)

        self.openButton = QPushButton('Open File', self)
        self.openButton.clicked.connect(self.open_file)
        layout.addWidget(self.openButton)

        central_widget.setLayout(layout)
        print("UI Initialized")

    def open_file(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.ReadOn
        file_path, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)", options=options)
        if file_path:
            model = load_stl(file_path)
            toolpath_type = self.toolpathComboBox.currentText()

            if toolpath_type == "Contour":
                toolpath = generate_contour_toolpath(model)
            elif toolpath_type == "Raster":
                toolpath = generate_raster_toolpath(model)
            elif toolpath_type == "Pocketing":
                toolpath = generate_pocketing_toolpath(model)
            elif toolpath_type == "Helical":
                toolpath = generate_helical_toolpath((0,0,0), 10, 0.5, 50)

            visualize_toolpath_with_model(model, toolpath, f"{toolpath_type} Toolpath")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cam_software = CAMSoftware()
    cam_software.show()
    sys.exit(app.exec_())
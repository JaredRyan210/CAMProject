import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from file_import import load_stl
from toolpath_generation import generate_toolpath
from visualization import visualize_toolpath

class CAMSoftware(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing UI")
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('CAM Software')
        self.setGeometry(100, 100, 800, 600)

        self.openButton = QPushButton('Open File', self)
        self.openButton.setGeometry(50, 50, 100, 30)
        self.openButton.clicked.connect(self.open_file)
        print("UI Initialized")

    def open_file(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.ReadOn
        file_path, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)", options=options)
        if file_path:
            model = load_stl(file_path)
            toolpath = generate_toolpath(model)
            visualize_toolpath(toolpath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cam_software = CAMSoftware()
    cam_software.show()
    sys.exit(app.exec_())
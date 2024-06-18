from gui import CAMSoftware
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    
    print("Starting application")
    app = QApplication(sys.argv)
    cam_sofware = CAMSoftware()
    print("Showing main window")
    cam_sofware.show()
    print("Entering main loop")
    sys.exit(app.exec_())
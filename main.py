import sys
import os
from PyQt5 import QtWidgets
from app.main_window import Ui_MainWindow

import controllers

class MSPyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MSPyApp, self).__init__()
        
        # Get controllers for app
        self.controllers = controllers.Controllers(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("MSPy - Manga and Novel Scraper")
        
        # Connect signals to slots
        self.ui.pushButton.clicked.connect(self.controllers.get_url_cover)
        self.ui.lineEdit.returnPressed.connect(self.controllers.get_url_cover)
        
        # Initialize the graphics scene
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        # Setup status bar
        self.status_label = QtWidgets.QLabel("Ready")
        self.statusBar().addWidget(self.status_label)
        
        # Create temp directory for downloaded images
        self.temp_dir = os.path.join(os.getcwd(), 'temp')
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
            
        # URL fetch thread
        # self.fetch_thread = None

def main():
    """Main application entry point"""
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Create and show the main window
    window = MSPyApp()
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
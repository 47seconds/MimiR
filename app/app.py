import os
from PyQt5 import QtWidgets
from app.main_window import Ui_MainWindow
from controllers import Controllers

class MSPyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MSPyApp, self).__init__()
        
        # Get controllers for app
        self.controllers = Controllers(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("MimiR - Manga and Novel Scraper")
        
        # Connect signals to slots
        self.ui.getButton.clicked.connect(self.controllers.get_url_cover)
        self.ui.urlLineEdit.returnPressed.connect(self.controllers.get_url_cover)
        
        # Initialize the graphics scene
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.coverGraphicsView.setScene(self.scene)
        
        # Setup status bar
        self.status_label = QtWidgets.QLabel("Ready")
        self.statusBar().addWidget(self.status_label)
        
        # Create temp directory for downloaded images
        self.temp_dir = os.path.join(os.getcwd(), 'temp')
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
            
        # Connect menu actions if needed
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
    
    def show_about_dialog(self):
        QtWidgets.QMessageBox.about(
            self,
            "About MimiR",
            "MimiR - An Open Source Manga and Novel Scraping Tool\n\n"
            "A lightweight application to download manga and novels from various sources."
        )
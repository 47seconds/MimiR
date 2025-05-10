from PyQt5 import QtWidgets, QtCore, QtGui
from repositories.url import Url_operations
from repositories.thread import Threading_operations
from repositories.graphic import Graphic_operations

class Controllers:
    def __init__(self, app_reference):
        self.app = app_reference
        self.url_operations = Url_operations()
        self.graphic_operations = Graphic_operations(self.app)
        
        self.fetch_thread = None
    
    def get_url_cover(self):
        url = self.app.ui.urlLineEdit.text().strip()
        
        if not url:
            self.app.status_label.setText("Please enter a valid URL")
            return
        
        # Disable the button and change cursor to waiting
        self.app.ui.getButton.setEnabled(False)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.app.status_label.setText(f"Fetching: {url}")
        
        # Create worker thread for fetching
        if self.fetch_thread is not None and self.fetch_thread.isRunning():
            self.fetch_thread.terminate()
        
        self.fetch_thread = Threading_operations(url, self.app.temp_dir)
        self.fetch_thread.finished.connect(self.graphic_operations.handle_fetch_finished)
        self.fetch_thread.error.connect(self.graphic_operations.handle_fetch_error)
        self.fetch_thread.start()
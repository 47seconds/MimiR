import os
from PyQt5 import QtWidgets, QtCore, QtGui

class Graphic_operations:
    def __init__(self, app_reference):
        self.app = app_reference
        
    def update_image(self, image_path):
        """Update the image in the graphics view"""
        if not os.path.exists(image_path):
            self.app.status_label.setText(f"Image not found: {image_path}")
            return
            
        pixmap = QtGui.QPixmap(image_path)
        if not pixmap.isNull():
            # Scale pixmap to fit the graphics view while maintaining aspect ratio
            pixmap = pixmap.scaled(
                self.app.ui.coverGraphicsView.width() - 10, 
                self.app.ui.coverGraphicsView.height() - 10,
                QtCore.Qt.KeepAspectRatio, 
                QtCore.Qt.SmoothTransformation
            )
            
            self.app.scene.clear()
            self.app.scene.addPixmap(pixmap)
            
            # Convert QRect to QRectF
            rect = pixmap.rect()
            self.app.scene.setSceneRect(QtCore.QRectF(rect))
            self.app.status_label.setText("Image loaded successfully")
        else:
            self.app.status_label.setText("Failed to load image")
            
    def handle_fetch_finished(self, image_path):
        """Handle successful URL fetch"""
        
        print("Fetching image done!")
        
        # Reset UI
        self.app.ui.getButton.setEnabled(True)
        QtWidgets.QApplication.restoreOverrideCursor()
        
        # Update the image if an image was downloaded
        if image_path:
            print(f"image path: {image_path}")
            self.update_image(image_path)
            # self.update_image(image_path)
        else:
            self.app.status_label.setText("No image found in the response")
    
    def handle_fetch_error(self, error_msg):
        """Handle fetch errors"""
        
        self.app.ui.pushButton.setEnabled(True)
        QtWidgets.QApplication.restoreOverrideCursor()
        self.app.status_label.setText(f"Error: {error_msg}")
        
        # Show error dialog
        QtWidgets.QMessageBox.critical(
            self.app,
            "Fetch Error",
            f"An error occurred while fetching the URL:\n{error_msg}"
        )
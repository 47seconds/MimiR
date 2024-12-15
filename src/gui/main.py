import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtCore import Qt
from src.grabber import getSource

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./src/gui/screens/Home.ui', self)
        
        self.download_button.clicked.connect(self.on_download_clicked)
        
    def on_download_clicked(self):
        url = self.site_text.text()
        details = getSource.get_source(url).get_details(url)
        
        if details:
            self.chapter_title_text.setText(details[0])
            self.chapter_count_text.setText(details[1])
            
            image_url = details[2]
            response = requests.get(image_url)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            scaled_pixmap = pixmap.scaled(
                self.novel_image.width(),
                self.novel_image.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.novel_image.setPixmap(scaled_pixmap)

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    demo = AppDemo()
    demo.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
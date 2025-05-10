import os
from utils.save_image_from_response import save_image_from_response
from repositories.url import Url_operations
from PyQt5.QtCore import QThread, pyqtSignal

class Threading_operations(QThread):
    """Worker thread for running URL fetch operations"""
    
    finished = pyqtSignal(str)  # Signal emitted when fetch is done, passes image path
    error = pyqtSignal(str)     # Signal emitted when an error occurs
    
    def __init__(self, url, temp_dir):
        super().__init__()
        self.url = url
        self.temp_dir = temp_dir
    
    def run(self):
        try:           
            # Check if URL is an image
            url_operations = Url_operations()
            response, content_type = url_operations.fetch_url(self.url)
            
            if 'image' in content_type:
                # URL is an image, download it
                img_path = os.path.join(self.temp_dir, 'temp_cover.jpg')
                save_image_from_response(img_path, response)
                self.finished.emit(img_path)
            else:
                # URL is not an image, return empty path
                self.finished.emit("")
                
        except Exception as e:
            self.error.emit(str(e))

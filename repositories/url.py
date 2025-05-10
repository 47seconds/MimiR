import requests

class Url_operations:
    def __init__(self):
        pass
        
    def fetch_url(self, url):
        """Fetch the URL entered by the user"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, stream=True)
        content_type = response.headers.get('Content-Type', '')
        
        return response, content_type
        
        # print("fetch_url called")
        
        # url = self.app.ui.lineEdit.text().strip()
        
        # if not url:
        #     self.app.status_label.setText("Please enter a valid URL")
        #     return
        
        # # Disable the button and change cursor to waiting
        # self.app.ui.pushButton.setEnabled(False)
        # QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        # self.app.status_label.setText(f"Fetching: {url}")
        
        # # Create worker thread for fetching
        # if self.app.fetch_thread is not None and self.app.fetch_thread.isRunning():
        #     self.app.fetch_thread.terminate()
        
        # self.app.fetch_thread = Threading_operations(url, self.app.temp_dir)
        # self.app.fetch_thread.finished.connect(self.graphics.handle_fetch_finished)
        # self.app.fetch_thread.error.connect(self.graphics.handle_fetch_error)
        # self.app.fetch_thread.start()
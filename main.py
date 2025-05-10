import sys
from PyQt5 import QtWidgets
from app.app import MSPyApp

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
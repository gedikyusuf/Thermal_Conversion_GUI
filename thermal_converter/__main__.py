# thermal_converter/__main__.py
import sys
from PyQt5.QtWidgets import QApplication
from .utils import log_message, Configuration
from .gui import FirstGui # gui.py dosyasındaki FirstGui sınıfını import eder

def main():
    """Application's main entry point."""
    log_message("--- ThermalConverter Application Starting Up ---")
    
    app = QApplication(sys.argv) 
    main_app = app 
    
    # Initialize Configuration object
    main_app.config = Configuration()

    # Start the first GUI
    main_app.first_gui = FirstGui(main_app)
    main_app.first_gui.show()

    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

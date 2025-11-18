# thermal_converter/utils.py
import os
from .exceptions import PathInitializationError, MissingDependencyError

def log_message(msg: str, log_file: str = "conversion_log.txt") -> None:
    """Prints the message to the console and writes it to the specified log file."""
    try:
        print(msg)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception as e:
        print(f"WARNING: Failed to write to log file: {e}")


class Configuration:
    """Manages application constants, window titles, and external tool paths centrally."""
    
    DEFAULT_LOG_FILE = "conversion_log.txt"
    DEFAULT_WINDOW_TITLE = "Thermal RJPG to TIFF Conversion Utility"
    
    STEP_TITLES = {
        1: 'STEP-1: Set Environment Variables (Path Initialization)',
        2: 'STEP-2: Generating RAW files (dji_irp.exe execution)',
        3: 'STEP-3: Convert RAW to TIFF (ImageJ Macro Execution)',
        4: 'STEP-4: ExifTool File Tag Copier (Metadata Transfer)',
        5: 'STEP-5: Process Completed'
    }
    
    def __init__(self):
        """Initializes Configuration object with all paths set to None."""
        self.root_folder = None
        self.dji_irp_path = None
        self.exiftool_exe_path = None
        self.imagej_executable = None
        self.macro_file = None
        log_message("Configuration object created.")

    def initialize_paths(self, root_folder: str) -> None:
        """Sets all required external tool paths based on the selected root folder."""
        if not root_folder or not os.path.isdir(root_folder):
            raise PathInitializationError(root_folder, "Root folder is invalid.")

        self.root_folder = root_folder
        self.dji_irp_path = os.path.join(root_folder, 'DJI_Thermal_SDK', 'utility', 'bin', 'windows', 'release_x64', 'dji_irp.exe')
        self.exiftool_exe_path = os.path.join(root_folder, 'exiftool', 'exiftool.exe')
        self.imagej_executable = os.path.join(root_folder, 'ImageJ', 'ImageJ', 'ImageJ.exe')
        self.macro_file = os.path.join(root_folder, 'ImageJ', 'ImageJ', 'macros', 'ysf.ijm')
        
        log_message(f"Configuration paths initialized for: {root_folder}")

    def validate_paths(self) -> None:
        """Validates the existence of critical external files."""
        required_files = {
            "DJI IRP": self.dji_irp_path,
            "ImageJ EXE": self.imagej_executable,
            "ImageJ MACRO": self.macro_file,
            "ExifTool EXE": self.exiftool_exe_path
        }
        
        for name, path in required_files.items():
            if not os.path.exists(path):
                raise MissingDependencyError(name, path)
        
        log_message("All external components validated successfully.")

import os
import sys
import shutil
import tempfile
import subprocess
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QFileDialog, QLabel, 
    QVBoxLayout, QWidget, QMessageBox
)

# Yeni modüler yapıdan importlar
from .utils import log_message, Configuration 
from .exceptions import PathInitializationError, MissingDependencyError, CommandExecutionError


class FirstGui(QMainWindow):
    """The first GUI for setting environment variables (STEP-1)."""
    
    def __init__(self, main_app):
        """Initializes the window and sets up components."""
        super().__init__()
        self.main_app = main_app
        self.root_folder = None
        self.layout = QVBoxLayout()
        
        self._setup_window()
        self._create_widgets()
        self._layout_widgets()
        self._connect_signals()
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def _setup_window(self):
        """Sets window title and basic configuration."""
        self.setWindowTitle(self.main_app.config.STEP_TITLES[1])

    def _create_widgets(self):
        """Creates all visual components."""
        self.folder_label = QLabel('Please select the root folder containing the SDK, ImageJ, and ExifTool.')
        self.select_folder_button = QPushButton('1. Select Root Folder (Browse Directory)')
        self.set_env_button = QPushButton('2. Set Paths, Verify Components, and Continue')

    def _layout_widgets(self):
        """Places components into the vertical layout."""
        self.layout.addWidget(self.folder_label)
        self.layout.addWidget(self.select_folder_button)
        self.layout.addSpacing(15)
        self.layout.addWidget(self.set_env_button)

    def _connect_signals(self):
        """Connects button clicks to corresponding methods."""
        self.select_folder_button.clicked.connect(self.select_folder)
        self.set_env_button.clicked.connect(self.set_env_vars)

    def select_folder(self):
        """Allows user to select the root folder and updates the label."""
        folder = QFileDialog.getExistingDirectory(self, 'Select Root Folder')
        if folder:
            self.root_folder = folder
            self.folder_label.setText(f'Root Folder SELECTED: {folder}')
            log_message(f"Selected root folder: {folder}")
        else:
            self.folder_label.setText("Folder selection cancelled or failed.")

    def set_env_vars(self):
        """Sets environment variables and verifies the existence of external files."""
        config = self.main_app.config
        try:
            # 1. Yolları Başlatma
            config.initialize_paths(self.root_folder)
            # 2. Yolları Doğrulama (Dosya Var Olan Kontrolleri)
            config.validate_paths()
        except (PathInitializationError, MissingDependencyError) as e:
            QMessageBox.critical(self, "Critical Error", f"Initialization Failed: {e}")
            log_message(f"CRITICAL ERROR: {e}")
            return
            
        log_message("STEP-1: All environment variables set and external components verified.")
        # Bir sonraki adıma geçiş
        self.main_app.second_gui = SecondGui(self.main_app)
        self.main_app.second_gui.show()
        self.close()


class SecondGui(QMainWindow):
    """The second GUI for generating RAW files (STEP-2)."""
    
    def __init__(self, main_app):
        """Initializes the window and sets up components."""
        super().__init__()
        self.main_app = main_app
        self.config = self.main_app.config
        self.layout = QVBoxLayout()
        self._setup_window()
        self._create_widgets()
        self._layout_widgets()
        self._connect_signals()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def _setup_window(self):
        """Sets window title."""
        self.setWindowTitle(self.config.STEP_TITLES[2])

    def _create_widgets(self):
        """Creates necessary visual components."""
        self.folder_label = QLabel(f'Root Folder: {self.config.root_folder}')
        self.description_label = QLabel('This step executes dji_irp.exe to convert all *.JPG files in the root folder to *.raw files.')
        self.run_command_button = QPushButton('2. Run DJI IRP (Generate RAW Files)')
    
    def _layout_widgets(self):
        """Places components into the layout."""
        self.layout.addWidget(self.folder_label)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.run_command_button)
        
    def _connect_signals(self):
        """Connects signals."""
        self.run_command_button.clicked.connect(self.run_command)

    def run_command(self):
        """Starts the RAW file generation process via Windows command prompt."""
        dji_irp_exe = self.config.dji_irp_path
        # Windows'a özgü toplu işlem komutu
        cmd_template = 'for %i in (*.JPG) do "{}" -a measure -s "%i" -o "%~ni.raw" --measurefmt float32'
        final_cmd = cmd_template.format(dji_irp_exe)
        
        try:
            # Komut istemcisini başlatma ve komutu gönderme
            subprocess.Popen(
                f'start cmd /K "cd /d {self.config.root_folder} & {final_cmd}"', 
                shell=True, 
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            log_message("STEP-2: RAW file generation command sent successfully via new CMD window.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Command execution failed: {e}")
            log_message(f"ERROR: Failed to launch command for RAW generation: {e}")
            return

        # Bir sonraki adıma geçiş
        self.main_app.third_gui = ThirdGui(self.main_app)
        self.main_app.third_gui.show()
        self.close()


class ThirdGui(QMainWindow):
    """The third GUI for RAW to TIFF conversion (STEP-3)."""
    
    def __init__(self, main_app):
        """Initializes the window and sets up components."""
        super().__init__()
        self.main_app = main_app
        self.config = self.main_app.config
        self.layout = QVBoxLayout()
        self._setup_window()
        self._create_widgets()
        self._layout_widgets()
        self._connect_signals()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def _setup_window(self):
        """Sets window title."""
        self.setWindowTitle(self.config.STEP_TITLES[3])

    def _create_widgets(self):
        """Creates necessary visual components."""
        self.folder_label = QLabel(f'Root Folder: {self.config.root_folder}')
        self.description_label = QLabel('This step launches ImageJ in headless mode to convert *.raw files to TIFF files using the ysf.ijm macro.')
        self.convert_button = QPushButton('3. Convert RAW to TIFF via ImageJ')
    
    def _layout_widgets(self):
        """Places components into the layout."""
        self.layout.addWidget(self.folder_label)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.convert_button)
        
    def _connect_signals(self):
        """Connects signals."""
        self.convert_button.clicked.connect(self.convert_files)

    def convert_files(self):
        """Executes ImageJ with the macro to perform batch TIFF conversion."""
        src_folder = self.config.root_folder
        dest_folder = os.path.join(src_folder, 'converted')
        
        # Çıktı klasörünü oluşturma
        try:
            os.makedirs(dest_folder, exist_ok=True)
        except OSError as e:
            QMessageBox.critical(self, "Error", f"Could not create output folder: {e}")
            log_message(f"ERROR: Failed to create output directory: {e}")
            return
            
        macro_arg = f"{src_folder}###{dest_folder}"
        temp_macro = os.path.join(tempfile.gettempdir(), "ysf_temp.ijm")
        
        # Makro dosyasını geçici dizine kopyalama
        try:
            shutil.copy2(self.config.macro_file, temp_macro)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Macro copy failed: {e}")
            log_message(f"ERROR: Macro copy failed: {e}")
            return
        
        # ImageJ başlatma komutu
        cmd = [self.config.imagej_executable, "--headless", "-macro", temp_macro, macro_arg]
        
        try:
            # Komutu senkron çalıştırıp sonucunu bekler
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            
            if result.returncode != 0:
                 log_message(f"STEP-3: ImageJ conversion error (code {result.returncode}). Stderr:\n{result.stderr}")
            else:
                 log_message("STEP-3: ImageJ conversion completed successfully.")
                 
            log_message(f"ImageJ Stdout:\n{result.stdout.strip()}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"ImageJ launch failed: {e}")
            log_message(f"STEP-3: Failed to launch ImageJ: {e}")
            return

        # Bir sonraki adıma geçiş
        self.main_app.fourth_gui = FourthGui(self.main_app)
        self.main_app.fourth_gui.show()
        self.close()


class FourthGui(QMainWindow):
    """The final GUI for EXIF tag copying (STEP-4)."""
    
    def __init__(self, main_app):
        """Initializes the window and sets up components."""
        super().__init__()
        self.main_app = main_app
        self.config = self.main_app.config
        self.layout = QVBoxLayout()
        self._setup_window()
        self._create_widgets()
        self._layout_widgets()
        self._connect_signals()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def _setup_window(self):
        """Sets window title."""
        self.setWindowTitle(self.config.STEP_TITLES[4])

    def _create_widgets(self):
        """Creates necessary visual components."""
        self.folder_label = QLabel(f'Source Folder: {self.config.root_folder}\nDestination Folder: {os.path.join(self.config.root_folder, "converted")}')
        self.description_label = QLabel('This step uses ExifTool to copy metadata from original JPGs to converted TIFF files.')
        self.copy_tags_button = QPushButton('4. Copy EXIF Tags with ExifTool')
        self.completion_label = QLabel('Click button to start metadata copy.')
    
    def _layout_widgets(self):
        """Places components into the layout."""
        self.layout.addWidget(self.folder_label)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.copy_tags_button)
        self.layout.addSpacing(15)
        self.layout.addWidget(self.completion_label)
        
    def _connect_signals(self):
        """Connects signals."""
        self.copy_tags_button.clicked.connect(self.copy_tags)

    def copy_tags(self):
        """Copies EXIF tags from original JPG files to converted TIF files."""
        source_folder = self.config.root_folder
        output_folder = os.path.join(source_folder, 'converted')
        
        try:
            JPG_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]
            if not JPG_files:
                self.completion_label.setText('ERROR: No (.JPG) files found in the source folder.')
                log_message('ERROR: No .JPG files found for tag copying.')
                return
        except FileNotFoundError:
            self.completion_label.setText(f'ERROR: Folder not found: {source_folder}')
            return

        self.completion_label.setText('Metadata copying started...')
        self.copy_tags_button.setEnabled(False) 
        successful_copies = 0
        
        for JPG_filename in JPG_files:
            base_name = os.path.splitext(JPG_filename)[0]
            JPG_path = os.path.join(source_folder, JPG_filename)
            dest_filename = base_name + '.TIF' 
            dest_path = os.path.join(output_folder, dest_filename)

            if not os.path.exists(dest_path):
                log_message(f'WARNING: Target TIF file not found: {dest_path}. Skipping tag copy.')
                continue

            # ExifTool komutu
            exiftool_cmd = [
                self.config.exiftool_exe_path,
                '-TagsFromFile',
                JPG_path,
                '-all:all', 
                '-overwrite_original', 
                dest_path
            ]
            
            try:
                subprocess.run(exiftool_cmd, capture_output=True, text=True, check=True)
                log_message(f'SUCCESS: Tags copied to {dest_filename}.')
                successful_copies += 1
            except subprocess.CalledProcessError as e:
                log_message(f'ERROR: Tag copy failed for ({JPG_filename}): {e.stderr.strip()}')
            except Exception as e:
                log_message(f'ERROR: ExifTool execution error: {e}')

        final_message = f'Process completed. Tags copied successfully for {successful_copies} out of {len(JPG_files)} files.'
        self.completion_label.setText(final_message)
        log_message(final_message)
        
        QMessageBox.information(self, "Finished", "All steps completed successfully. Converted files are in the 'converted' folder.")
        self.copy_tags_button.setEnabled(True)

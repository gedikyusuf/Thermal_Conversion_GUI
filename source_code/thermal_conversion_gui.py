import os
import sys
import shutil
import tempfile
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget

def log_message(msg):
    print(msg)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

class FirstGui(QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle('STEP-1: Set Environment Variables')

        self.layout = QVBoxLayout()
        self.folder_label = QLabel('No root folder selected')
        self.layout.addWidget(self.folder_label)

        self.select_folder_button = QPushButton('Select Root Folder')
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        self.set_env_button = QPushButton('Set Env Vars and Continue')
        self.set_env_button.clicked.connect(self.set_env_vars)
        self.layout.addWidget(self.set_env_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Root Folder')
        if folder:
            self.folder_label.setText(f'Root Folder: {folder}')
            self.root_folder = folder

    def set_env_vars(self):
        if not hasattr(self, 'root_folder') or not self.root_folder:
            self.folder_label.setText("Please select root folder first!")
            return

        self.main_app.root_folder = self.root_folder
        self.main_app.dji_folder = os.path.join(self.root_folder, 'DJI_Thermal_SDK', 'utility', 'bin', 'windows', 'release_x64')
        self.main_app.exiftool_folder = os.path.join(self.root_folder, 'exiftool')
        self.main_app.imagej_executable = os.path.join(self.root_folder, 'ImageJ', 'ImageJ', 'ImageJ.exe')
        self.main_app.macro_file = os.path.join(self.root_folder, 'ImageJ', 'ImageJ', 'macros', 'ysf.ijm')

        log_message(f"STEP-1: Env vars set for {self.root_folder}")
        self.main_app.second_gui = SecondGui(self.main_app, self.root_folder)
        self.main_app.second_gui.show()
        self.close()


class SecondGui(QMainWindow):
    def __init__(self, main_app, root_folder):
        super().__init__()
        self.main_app = main_app
        self.root_folder = root_folder
        self.setWindowTitle('STEP-2: Generating RAW files')

        self.layout = QVBoxLayout()
        self.folder_label = QLabel(f'DJI Folder: {self.root_folder}')
        self.layout.addWidget(self.folder_label)

        self.run_command_button = QPushButton('Generate RAW Files')
        self.run_command_button.clicked.connect(self.run_command)
        self.layout.addWidget(self.run_command_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def run_command(self):
        # dji_irp.exe'nin tam yolu
        dji_irp_exe = os.path.join(self.main_app.dji_folder, 'dji_irp.exe')
        if not os.path.exists(dji_irp_exe):
            self.folder_label.setText(f"dji_irp.exe not found at {dji_irp_exe}")
            return

        cmd = f'for %i in (*.JPG) do "{dji_irp_exe}" -a measure -s "%i" -o "%~ni.raw" --measurefmt float32'
        subprocess.Popen(f'start cmd /K "cd /d {self.root_folder} & {cmd}"', shell=True)
        log_message("STEP-2: RAW file generation command sent.")

        # Step-3 GUI'ye geçiş
        self.main_app.third_gui = ThirdGui(self.main_app, self.root_folder)
        self.main_app.third_gui.show()
        self.close()

class ThirdGui(QMainWindow):
    def __init__(self, main_app, root_folder):
        super().__init__()
        self.main_app = main_app
        self.root_folder = root_folder
        self.setWindowTitle('STEP-3: Convert RAW to TIFF')

        self.layout = QVBoxLayout()
        self.folder_label = QLabel(f'Root folder: {self.root_folder}')
        self.layout.addWidget(self.folder_label)

        self.convert_button = QPushButton('Convert RAW to TIFF')
        self.convert_button.clicked.connect(self.convert_files)
        self.layout.addWidget(self.convert_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def convert_files(self):
        src_folder = self.root_folder
        dest_folder = os.path.join(src_folder, 'converted')
        os.makedirs(dest_folder, exist_ok=True)
        macro_arg = f"{src_folder}###{dest_folder}"

        temp_macro = os.path.join(tempfile.gettempdir(), "ysf.ijm")
        shutil.copy2(self.main_app.macro_file, temp_macro)

        try:
            cmd = [self.main_app.imagej_executable, "--headless", "-macro", temp_macro, macro_arg]
            result = subprocess.run(cmd, capture_output=True, text=True)
            log_message(f"STEP-3: ImageJ output:\n{result.stdout}\n{result.stderr}")
        except Exception as e:
            log_message(f"STEP-3: Failed to launch ImageJ: {e}")

        self.main_app.fourth_gui = FourthGui(self.main_app, self.root_folder)
        self.main_app.fourth_gui.show()
        self.close()

class FourthGui(QMainWindow):
    def __init__(self, main_app, root_folder):
        super().__init__()
        self.main_app = main_app
        self.root_folder = root_folder
        self.setWindowTitle('STEP-4: ExifTool File Tag Copier')

        self.layout = QVBoxLayout()
        self.folder_label = QLabel(f'Root Folder: {self.root_folder}')
        self.layout.addWidget(self.folder_label)

        self.copy_tags_button = QPushButton('Copy EXIF Tags')
        self.copy_tags_button.clicked.connect(self.copy_tags)
        self.layout.addWidget(self.copy_tags_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def copy_tags(self):
        output_folder = os.path.join(self.root_folder, 'converted')
        os.makedirs(output_folder, exist_ok=True)

        JPG_files = [f for f in os.listdir(self.root_folder) if f.endswith('.JPG')]
        if not JPG_files:
            self.folder_label.setText('No .JPG files found.')
            return

        for JPG in JPG_files:
            JPG_path = os.path.join(self.root_folder, JPG)
            dest_filename = os.path.splitext(JPG)[0] + '.TIF'
            dest_path = os.path.join(output_folder, dest_filename)

            cmd = f'exiftool -TagsFromFile "{JPG_path}" -all:all "{dest_path}"'
            try:
                result = subprocess.run(cmd, shell=True, check=True)
                log_message(f'Tags copied from {JPG_path} to {dest_path} (code {result.returncode})')
            except subprocess.CalledProcessError as e:
                log_message(f'Error copying tags for {JPG}: {e}')

        log_message(f'Process completed. Files saved in: {output_folder}')

def main():
    app = QApplication([])
    main_app = app
    main_app.root_folder = None
    main_app.dji_folder = None
    main_app.imagej_executable = None
    main_app.macro_file = None

    main_app.first_gui = FirstGui(main_app)
    main_app.first_gui.show()

    app.exec_()

if __name__ == '__main__':
    main()

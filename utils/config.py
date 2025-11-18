# utils/config.py
"""
Small config holder. Users can edit or pass a path to a JSON/YAML config in future.
"""
from dataclasses import dataclass, field
import os

@dataclass
class Config:
    root_folder: str = field(default=None)
    dji_folder: str = field(default=None)
    exiftool_path: str = field(default="exiftool")  # assume on PATH
    imagej_executable: str = field(default=None)
    macro_file: str = field(default=None)
    output_folder: str = field(default="converted")
    temp_dir: str = field(default=os.path.join(os.getcwd(), "tmp"))

    def resolve_paths_from_root(self):
        if self.root_folder:
            self.dji_folder = os.path.join(self.root_folder, 'DJI_Thermal_SDK', 'utility', 'bin', 'windows', 'release_x64')
            self.exiftool_path = os.path.join(self.root_folder, 'exiftool') if os.path.exists(os.path.join(self.root_folder, 'exiftool')) else self.exiftool_path
            self.imagej_executable = os.path.join(self.root_folder, 'ImageJ', 'ImageJ', 'ImageJ.exe')
            self.macro_file = os.path.join(self.root_folder, 'ImageJ', 'ImageJ', 'macros', 'ysf.ijm')
            self.output_folder = os.path.join(self.root_folder, self.output_folder)

Thermal Conversion GUI (Modular Version)

A graphical and command-line tool for converting DJI radiometric R-JPEG thermal images into georeferenced TIFF products using ImageJ, DJI Thermal SDK, and ExifTool.

This repository includes:

A modular Python source code package (source_code/)

A GUI application for step-by-step thermal conversion

A CLI interface for batch processing

A pre-compiled Windows executable (tc.exe)

🚀 Quick Start (GUI)
1. Install Python and dependencies
pip install PyQt5


(Optional, if you add requirements.txt)

pip install -r requirements.txt

2. Install required external tools

These tools must be present in the project root folder or added to your system PATH:

✓ ImageJ

Download and extract to:
ImageJ/ImageJ.exe
https://wsr.imagej.net/distros/win/ij154-win-java8.zip

✓ DJI Thermal SDK

Extract to:
DJI_Thermal_SDK/
https://terra-1-g.djicdn.com/.../dji_thermal_sdk_v1.7_20241205.zip

✓ ExifTool

Extract to root and rename executable as:
exiftool.exe
https://exiftool.org/

🖥️ How to Use (GUI Workflow)

Launch ImageJ.exe once so that the environment initializes.

Start the program:

Either double-click tc.exe, or

Run the Python GUI from source:

python source_code/thermal_conversion_gui.py


Step 1: Select the folder containing R-JPEG thermal images → click Set Env Vars and Continue.

Step 2: Click Generate RAW Files (DJI SDK processing).

Step 3: Click Convert JPG to TIFF (ImageJ processing).

Step 4: Click Complete the Process.

Output will be saved in the Converted/ folder.
Each image will generate:

*.tiff → final converted image

*_original.tiff → optional intermediate file (can be deleted)

🧪 Command-Line Interface (CLI)

The modular Python version includes a CLI script:

python -m source_code.cli --input INPUT_FOLDER --output OUTPUT_FOLDER


(If you want, you can later expand this section.)

📂 Source Code Layout
source_code/
│── gui/                    # GUI components
│── processing/             # RAW creation + TIFF conversion modules
│── utils/                  # helpers for paths, logging, environment checks
│── cli.py                  # batch-processing interface
│── thermal_conversion_gui.py  # launches GUI


The executable tc.exe is compiled from this Python code.

📜 Citation

If you use this software, please cite:

Gedik, Y., & Ozcan, O. (2025). Thermal Conversion GUI (v1.0.0). Zenodo.
https://doi.org/10.5281/zenodo.17075877

🙏 Acknowledgements

ThermImageJ – Glenn J. Tattersall (2019).
https://doi.org/10.5281/zenodo.2652896

ImageJ – Public Domain License
https://imagej.net

ExifTool – Artistic License
https://exiftool.org

DJI Thermal SDK – SDK License Agreement
DJI official distribution

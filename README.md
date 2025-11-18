# Thermal Conversion GUI  
*A modular workflow for converting DJI R-JPEG thermal imagery to radiometric TIFF*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17075877.svg)](https://doi.org/10.5281/zenodo.17075877)

---

## 🌡️ Overview

**Thermal Conversion GUI** is a modular Python-based workflow that automates the full conversion pipeline of DJI R-JPEG thermal images into radiometric, georeferenced TIFF files.

It integrates:

- DJI *Thermal SDK* → RAW extraction  
- *ImageJ (ThermImageJ)* → RAW → TIFF float32 conversion  
- *ExifTool* → Metadata transfer  
- A complete **PyQt5 GUI**  
- A **CLI module** for batch processing  
- Modular source code for reproducibility  

The GUI version is also released as a standalone executable: `tc.exe`.

---

## 🚀 Quick Start (GUI)

### 1. Requirements (Python 3.9+)
Install dependencies:

```bash
pip install -r requirements.txt


2. Required external tools

Download and place these inside your root folder:

✔️ ImageJ

Download:
https://wsr.imagej.net/distros/win/ij154-win-java8.zip

Extract as:
<root>/ImageJ/ImageJ.exe

✔️ DJI Thermal SDK

Download:
https://terra-1-g.djicdn.com/.../dji_thermal_sdk_v1.7_20241205.zip

Extract as:
<root>/DJI_Thermal_SDK/


✔️ ExifTool

Download:
https://sourceforge.net/projects/exiftool/files/
Extract and rename:
exiftool(-k).exe → exiftool.exe


GUI Workflow
Step 1 — Select folder

Choose the folder with your thermal images and set environment variables.

Step 2 — Generate RAW files

The tool executes DJI dji_irp.exe to create .raw files.

Step 3 — Convert RAW → TIFF

Runs ImageJ + ThermImageJ macro headlessly.

Step 4 — Metadata transfer

EXIF metadata copied from JPG → final TIFF.

Output saved in:
<root>/converted/

Source Code

The modular source code is located in:
source_code/

Main application entry point:
source_code/thermal_conversion_gui.py
The released Windows executable (tc.exe) was compiled from this script.

Citation
If you use this software, please cite:
Gedik, Y., & Ozcan, O. (2025). Thermal Conversion GUI (v1.0.0). Zenodo.
https://doi.org/10.5281/zenodo.17075877

Acknowledgements

ThermImageJ – Glenn J. Tattersall
https://doi.org/10.5281/zenodo.2652896

ImageJ – Public Domain

ExifTool – Artistic License

DJI Thermal SDK – DJI SDK License Agreement

---

#

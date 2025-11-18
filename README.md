# Workflow Automation for UAV Thermal Image Conversion and Geospatial Modeling

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17075877.svg)](https://doi.org/10.5281/zenodo.17075877)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Thermal Conversion GUI** is an open-source tool that automates conversion of DJI radiometric R-JPEG thermal images into georeferenced, radiometrically-correct TIFF files suitable for GIS and photogrammetric workflows. It provides both a user-friendly GUI (Windows executable `tc.exe`) and a modular Python implementation for review and batch processing.

---

## 🔎 Overview

- Convert DJI R-JPEG (radiometric JPEG) → 16-bit / float TIFF while preserving embedded temperature metadata and EXIF geotags.  
- Integrates: DJI Thermal SDK, ImageJ (ThermImageJ macros), and ExifTool into a single automated pipeline.  
- Offers: GUI for one-click workflows and CLI for automated batch runs.  
- Source code available in: `source_code/thermal_conversion_gui/`

---

## 📦 Badges & Citation

If you use this software, please cite:

**Gedik, Y., & Ozcan, O. (2025). Workflow Automation for UAV Thermal Image Conversion and Geospatial Modeling (v1.0.0). Zenodo.**  
https://doi.org/10.5281/zenodo.17075877

---

## ⚙️ Requirements

- Python 3.9+  
- Windows recommended for DJI raw generation (dji_irp.exe) — ImageJ headless and ExifTool are cross-platform.  
- System tools (external, *not* pip):  
  - ImageJ (https://imagej.net)  
  - ExifTool (https://exiftool.org)  
  - DJI Thermal SDK (download from DJI)

**Python packages** (install with `pip`):
```bash
pip install -r requirements.txt

Example requirements.txt entries:
PyQt5>=5.15.7
numpy>=1.23.0
pillow>=10.0.0
psutil>=5.9.0

🔧 Installation (Step-by-step)
1. Clone repository:
git clone https://github.com/gedikyusuf/Thermal_Conversion_GUI.git
cd Thermal_Conversion_GUI

2.Create virtualenv (optional but recommended):
pip install -r requirements.txt

3.Install Python dependencies:
pip install -r requirements.txt


4.Download and place external tools under your chosen root folder (or add to PATH):

ImageJ
Download and extract, e.g. place as <root>/ImageJ/ImageJ.exe.
Example: https://wsr.imagej.net/distros/win/ij154-win-java8.zip

DJI Thermal SDK
Extract the SDK and ensure dji_irp.exe is available under:
<root>/DJI_Thermal_SDK/utility/bin/windows/release_x64/dji_irp.exe

ExifTool
Download, extract and ensure exiftool.exe is accessible (either in root or in PATH).
https://exiftool.org/

Tip: If you place ImageJ, DJI SDK and ExifTool inside the same chosen root folder, the GUI will auto-detect them (Step 1).

▶️ Quick Start — GUI (recommended for non-programmers)
1.Ensure ImageJ is launched at least once (so it initializes).
2.Double-click tc.exe in repository root OR run the Python GUI:
python source_code/run_gui.py
3.Follow the four steps in the GUI:

Step 1 — Set Environment: select the root folder containing your ImageJ/, DJI_Thermal_SDK/, and exiftool.exe.

Step 2 — Generate RAW files: runs dji_irp.exe to extract radiometric .raw files. (Windows-only step)

Step 3 — Convert RAW → TIFF: runs ImageJ in headless mode using the included ThermImageJ macro to produce TIFFs.

Step 4 — Copy EXIF tags: uses ExifTool to copy GPS and timestamp metadata from original JPG to final TIFFs.

Output is saved to:
<root>/converted/

▶️ Quick Start — CLI (batch processing)
Run the full pipeline headlessly (useful for servers / scripted runs):
python -m source_code.cli --root "C:\path\to\root" --imagej "C:\path\to\ImageJ.exe" --exiftool "C:\path\to\exiftool.exe"

🧩 How it works (technical summary)

The workflow integrates three main stages:

Radiometric extraction (DJI Thermal SDK)
Uses dji_irp.exe to extract floating point radiometric measurements from R-JPEG into .raw files.

Conversion (ImageJ + ThermImageJ macro)
Converts .raw into TIFF images (float or 16-bit) preserving radiometric values and optionally applying macros for scaling or clipping.

Metadata transfer (ExifTool)
Copies EXIF metadata (GPS, timestamp) from original JPG to converted TIFF to preserve geolocation for photogrammetry/GIS.

All steps are wrapped by a Python GUI and modular core modules so the same pipeline can be run programmatically (CLI) or via interactive GUI.

✅ Output & Post-processing notes

Converted TIFFs are stored in <root>/converted/. For each input JPG you will typically see:

image_name.TIF (final, geotagged)

image_name.TIF_original (intermediate, can be removed)

Typical performance: depends on CPU, disk, and ImageJ processing; converting ~100 images often completes within a few minutes on a modern laptop (times will vary).

🛠 Troubleshooting

dji_irp.exe not found — ensure DJI SDK path is correctly placed inside the selected root folder or update config to point to the executable.

ImageJ macro fails — open ImageJ manually and run the macro with a sample image to check macro compatibility and required plugins.

ExifTool errors — verify exiftool.exe is executable (Windows may show exiftool(-k).exe, rename to exiftool.exe).

Permissions — run GUI with appropriate file-system permissions for reading/writing the folders.

🧪 Tests & Reproducibility

The repository includes a modular Python package in source_code/ so reviewers can inspect, run and test the pipeline.

A command-line pipeline is provided to enable automated testing in CI or cluster environments.

📖 Citation

If you use this software, please cite:
Gedik, Y., & Ozcan, O. (2025). Thermal Conversion GUI (v1.0.0). Zenodo.
https://doi.org/10.5281/zenodo.17075877

📚 References & Acknowledgements

Tattersall, G. J. (2019). ThermImageJ: Thermal Image Functions and Macros for ImageJ. https://doi.org/10.5281/zenodo.2652896

Schneider, C. A., Rasband, W. S., & Eliceiri, K. W. (2012). NIH Image to ImageJ: 25 years of image analysis. Nature Methods.

ExifTool — Phil Harvey (2025). https://exiftool.org

DJI Thermal SDK — DJI Technology Co., Ltd. (2023).

🧾 License

This project is distributed under the MIT License. See LICENSE file for details.

💬 Contact

For questions, bug reports or collaboration:
Yusuf Gedik — gediky21@itu.edu.tr

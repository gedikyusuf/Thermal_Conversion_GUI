# Workflow Automation for UAV Thermal Image Conversion and Geospatial Modeling

Thermal Conversion GUI is an open-source tool that automates conversion of DJI radiometric R-JPEG thermal images into georeferenced, radiometrically-correct TIFF files suitable for GIS and photogrammetric workflows. It provides a user-friendly GUI and a **modular Python package implementation** for review and automated batch processing.

---

## 🔎 Overview

* Convert DJI R-JPEG (radiometric JPEG) → 16-bit / float TIFF while preserving embedded temperature metadata and EXIF geotags.
* Integrates: **DJI Thermal SDK**, **ImageJ** (ThermImageJ macros), and **ExifTool** into a single automated pipeline.
* Offers: GUI for one-click workflows and CLI for automated batch runs.

---

## 📦 Badges & Citation

If you use this software, please cite:
Gedik, Y., & Ozcan, O. (2025). Workflow Automation for UAV Thermal Image Conversion and Geospatial Modeling (v1.0.0). Zenodo.
`https://doi.org/10.5281/zenodo.17075877`

---

## ⚙️ Requirements

* **Python 3.9+**
* Windows recommended for DJI raw generation (`dji_irp.exe`).
* **System tools (external, must be placed in root folder):**
    * **ImageJ** (`https://imagej.net`)
    * **ExifTool** (`https://exiftool.org`)
    * **DJI Thermal SDK** (Download from DJI)
* **Python packages** (install with `pip`):
    * Dependencies are listed in `setup.py`.

---

## 🔧 Installation

1.  **Clone repository:**
    ```bash
    git clone [https://github.com/gedikyusuf/Thermal_Conversion_GUI.git](https://github.com/gedikyusuf/Thermal_Conversion_GUI.git)
    cd Thermal_Conversion_GUI
    ```

2.  **Create virtualenv** (optional but recommended).

3.  **Install the Python package:**
    ```bash
    pip install .
    ```

4.  **Download and place external tools** (ImageJ, DJI SDK, ExifTool) inside your chosen root processing folder. The GUI will use the paths defined in `thermal_converter/utils.py` to auto-detect them.

---

## ▶️ Quick Start — Using the Application

### GUI (Interactive Workflow)
Launch the application using the entry point defined in `setup.py`:
```bash
thermalconverter

Follow the four automated steps (Set Environment, Generate RAW, Convert TIFF, Copy EXIF tags).

CLI (Batch Processing)
Run the full pipeline headlessly using the package entry module (useful for servers / scripted runs):
python -m thermal_converter --root "C:\path\to\root" --imagej "C:\path\to\ImageJ.exe" --exiftool "C:\path\to\exiftool.exe"

🧪 Tests & Reproducibility

The core logic is structured as a modular Python package (thermal_converter/) and includes automated tests in the tests/ directory to ensure correctness and reproducibility across different environments.

To run the tests, install pytest and execute:
pip install pytest pytest-mock
pytest

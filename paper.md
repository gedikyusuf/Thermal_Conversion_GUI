---
title: "Workflow Automation for UAV Thermal Image Conversion and Geospatial Modeling"
authors:
  - name: Yusuf Gedik
    orcid: 0009-0004-8998-3978
    affiliation: 1
  - name: Orkan Ozcan
    orcid: 0000-0002-7485-6157
    affiliation: 1
affiliations:
  - name: Eurasia Institute of Earth Sciences, Istanbul Technical University, Istanbul, Türkiye
    index: 1
date: 2025-09-08
repository: "https://github.com/gedikyusuf/Thermal_Conversion_GUI"
---

# Summary
Thermal imaging has become increasingly important in structural health monitoring, geosciences, and ecological observations, particularly with the growing accessibility of UAV-based remote sensing platforms [@mccafferty2021]. Most commercial UAV thermal cameras record data in Radiometric JPEG (R-JPEG) format, embedding raw temperature values in metadata rather than storing them in a geospatially compatible raster format that can be directly processed by GIS software.

Several tools exist for thermal extraction workflows, including ImageJ-based macros [@tattersall2019] and radiometric metadata decoders such as ExifTool [@harvey2025]. However, these solutions typically require scripting experience, manual orchestration across multiple software steps, or command-line data handling, which significantly increases the risk of user error and slows down large-scale processing.

The software presented here provides a single-step, unified GUI and CLI-based workflow that converts UAV R-JPEG files into radiometrically calibrated and GIS-ready TIFF rasters. The automated conversion process greatly reduces manual effort and processing time, which are common challenges in large-scale or time-sensitive projects. Furthermore, the robust, modular Python package architecture ensures high code quality, automated testing, and operational efficiency for research involving high-throughput thermal remote sensing.

# Statement of Need
Thermal imagery workflows in scientific and engineering applications often involve fragmented pipelines, requiring users to manually coordinate radiometric metadata extraction, image conversion, and GIS integration using multiple independent tools [@schneider2012]. In traditional methods, thousands of R-JPEG files are usually converted manually, causing significant time loss and workload. This process depends heavily on the user and is prone to inconsistencies.
This software addresses this gap by integrating essential, industry-standard tools:
R-JPEG decoding (DJI Thermal SDK compliant)
Automated raster export (via ImageJ headless processing)
Metadata preservation and GIS-compatible georeferencing (via ExifTool)
into a single executable interface. The tool has already been successfully applied in UAV-based structural monitoring workflows [@ozcan2023; @kara2023] and post-earthquake mapping studies [@karakas2025], demonstrating its substantial utility in civil engineering and geoscience applications. This automated data conversion workflow facilitates accurate, repeatable, and spatially detailed thermal analyses, strengthening data-driven decision-making in multidisciplinary research contexts.


# Key Features
The core functionality of the ThermalConverter is delivered through a robust Python package architecture that emphasizes modularity and user accessibility:
Unified Pipeline Orchestration: The tool acts as a single-step pipeline orchestrator, managing the sequential execution of external tools necessary for R-JPEG processing. This approach minimizes user intervention compared to traditional fragmented workflows, which drastically improves data consistency.
Dual Execution Interface: For maximum utility, the software provides a dual execution interface. It offers a GUI-based execution for researchers who require an intuitive, non-coding environment, and a dedicated Command-Line Interface (CLI) for server-side batch processing and integration into larger scripted workflows.
Robust Metadata Preservation: During conversion, the tool preserves the geographic reference and thermal data contained in the R-JPEG images, ensuring high accuracy and scientific reliability for further image processing and numerical analysis steps.
Open Architecture: The core logic is structured into dedicated modules for error handling (exceptions.py), path management (utils.py), and a modular application core, designed for maintainable extension and integration into larger automated research pipelines.

# Implementation and Architecture
The software is implemented in Python 3.9+ and uses PyQt5 to provide the graphical user interface. The architecture follows a clean separation of concerns, divided into three main stages managed by distinct modules:
Configuration and Validation: The utils.py module manages path initialization and performs rigorous checks on the input root directory to verify the presence of all required executables (DJI IRP, ImageJ, ExifTool). All validation failures result in dedicated custom exceptions defined in exceptions.py.
Conversion Stages: The core processing relies on calling three external utilities via the subprocess module:
Radiometric Extraction: Uses the DJI Thermal SDK utility (dji_irp.exe) to convert R-JPEG files into floating-point .raw files.
Raster Conversion: Uses ImageJ in headless mode, executing a custom macro to convert the .raw data into 16-bit TIFF format.
Georeferencing: Uses ExifTool to copy embedded EXIF and GPS metadata from the original R-JPEG files to the newly generated TIFF rasters.
User Interaction: The user interface (managed by gui.py) is structured into four sequential steps, guiding the user through the conversion pipeline. The CLI component uses argparse to replicate this entire sequential workflow without any GUI dependency, making it suitable for high-throughput computing environments.
# Acknowledgements
The authors gratefully acknowledge the Earth3Bee Lab – 3D Earth Modeling Laboratory for providing access to facilities and resources that supported the image processing tasks. We also acknowledge the open-source community behind ImageJ, ExifTool, and the PyQt5 framework that underpin this application. This work was supported by research grant from the Scientific and Technological Research Council of Türkiye

# References

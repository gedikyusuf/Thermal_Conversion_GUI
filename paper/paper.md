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

Thermal imaging has become increasingly important in structural health monitoring, geosciences, and ecological observations, particularly with the growing accessibility of UAV-based remote sensing platforms [@mccafferty2021]. Most commercial UAV thermal cameras record data in **radiometric JPEG (R-JPEG)** format, embedding temperature values in metadata rather than storing them in a geospatially compatible raster format.

Several tools exist for thermal extraction workflows, including ImageJ-based macros [@tattersall2019] and radiometric metadata decoders such as ExifTool [@harvey2025]. However, these solutions typically require scripting experience, multiple software steps, or manual data handling, which can increase user error and slow down large-scale processing.

The software presented here provides a **single-step, GUI-based workflow** that converts UAV R-JPEG files into radiometrically calibrated and GIS-ready TIFF rasters without requiring any programming knowledge. The tool also supports batch processing, metadata parsing, and automated temperature extraction, improving reproducibility and operational efficiency for research involving thermal remote sensing.

# Statement of need

Thermal imagery workflows in scientific and engineering applications often involve fragmented pipelines, requiring users to extract radiometric metadata, convert images, and perform GIS integration using multiple independent tools [@schneider2012]. Existing solutions such as macro-based thermal extraction in ImageJ are powerful, but they require manual configuration and do not provide a fully automated UAV-focused batch workflow.

This software addresses this gap by integrating:

- R-JPEG decoding  
- Metadata-based temperature extraction  
- Automated raster export  
- Optional ImageJ macro processing  
- GIS-compatible georeferencing  

into a single executable interface. The tool has already been applied in UAV-based structural monitoring workflows [@ozcan2023; @kara2023] and post-earthquake mapping studies [@karakas2025], demonstrating its usefulness in both engineering and geoscience applications.

# Key features

- One-click batch conversion of UAV R-JPEG to temperature-calibrated TIFF
- GUI-based execution: no coding or scripting knowledge required
- Embedded use of ExifTool and ImageJ macro logic inside a unified workflow
- Automatically parses sensor metadata (DJI thermal SDK compliant [@dji2023])
- Produces geospatially compatible output for GIS or Python workflows
- Open-source Python implementation, extensible for research automation

# Acknowledgements

The authors gratefully acknowledge the Earth3Bee Lab – 3D Earth Modeling Laboratory for providing access to facilities and resources that supported the image processing tasks.  
(No external funding to declare.)

# References

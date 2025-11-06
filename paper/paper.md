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
McCafferty, D.J., Koprowski, R., Herborn, K., Tattersall, G.J., Jerem, P., Nord, A., 2021. Editorial: Advances in thermal imaging. Journal of Thermal Biology, 102, 103109. https://doi.org/10.1016/j.jtherbio.2021.103109. Available at: https://www.sciencedirect.com/science/article/pii/S0306456521002771.
Harvey, P., 2025. ExifTool version 12.80. Retrieved August 2025, from https://exiftool.org.
Glenn J. Tattersall. 2019. ThermImageJ: Thermal Image Functions and Macros for ImageJ. https://doi.org/10.5281/zenodo.2652896.
DJI Thermal SDK Documentation. DJI Technology Co., Ltd., 2023. Retrieved from https://www.dji.com/global/downloads/softwares/dji-thermal-sdk.
Schneider, C. A., Rasband, W. S., & Eliceiri, K. W., 2012. NIH Image to ImageJ: 25 years of image analysis. Nature Methods, 9, 671–675. https://doi.org/10.1038/nmeth.2089.
Özcan, O., Ozcan, O., & Erten, E., 2023. Integration of InSAR with UAV-based infrared thermography for bridge monitoring. In AGU Fall Meeting 2023 (NH32B-04), San Francisco, CA. American Geophysical Union.
N. Kara, H. A. Şişman, O. Özcan, O. Özcan and E. Erten, "InSAR Coupled with UAV-Based Infrared Thermography in the Context of Bridge Monitoring," IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium, Pasadena, CA, USA, 2023, pp. 5758-5761, https://doi.org/10.1109/IGARSS52108.2023.10282331.
Karakaş, M., Yıldırım, C., Ozcan, O., Akay, S. S., Gedik, Y. & Baka, Ç. M., 2025. High-resolution thermal imaging of the surface rupture of the February 6 2023, Kahramanmaraş earthquake (Mw 7.8), Türkiye. In EGU General Assembly 2025 (EGU25-11894). Copernicus Meetings. https://doi.org/10.5194/egusphere-egu25-11894.

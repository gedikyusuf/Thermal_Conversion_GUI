# Thermal Conversion GUI
Radiometric JPEG to TIFF conversion process

[![10.5281/zenodo.17075877](https://zenodo.org/badge/DOI/10.5281/zenodo.17075877.svg)](https://doi.org/10.5281/zenodo.17075877)

This repository contains the Thermal Conversion GUI, a tool developed for converting and processing thermal images captured by DJI devices.  

## Citation

If you use this tool in your research, please cite:

> Yusuf Gedik & Orkan Özcan (2025). **Thermal Conversion GUI**. Zenodo.  
> [https://doi.org/10.5281/zenodo.17075877](https://doi.org/10.5281/zenodo.17075877)


1-Before running the code, please download and set up the required programs as follows:

  ImageJ: Download from https://wsr.imagej.net/distros/win/ij154-win-java8.zip and extract under the selected root folder as ImageJ/ImageJ.exe.

  DJI Thermal SDK: Download from https://terra-1-g.djicdn.com/2640963bcd8e45c0a4f0cb9829739d6b/TSDK/v1.7(12.0-WA345T)/dji_thermal_sdk_v1.7_20241205.zip and extract under the selected root folder as DJI_Thermal_SDK/.

  ExifTool: Download from https://sourceforge.net/projects/exiftool/files/exiftool-13.34_64.zip/download, extract under the selected root folder, and rename exiftool(-k).exe to exiftool.exe.

  After completing these steps, launch ImageJ.exe and then run the program by double-clicking TC.exe.

2-In the window that opens, go to Step 1: click the "Select Thermal Images Folder" button and choose the folder containing your thermal images. Then, click the "Set Env Vars and Continue" button.

3-In the automatically opened Step 2 tab, click the "Generate RAW Files" button. A command-line window will appear, and the program will start generating .RAW files for your images. Please wait until this process is completed.

4-After that, in the automatically opened Step 3 tab, click the "Convert Files from JPG to TIFF" button.

5-In the automatically opened Step 4 tab, click the "Complete the Process" button to start the final processing step. The processing time depends on the number and size of your images (e.g., converting 100 thermal images typically takes about 5 minutes. In the Converted folder, two files will be created for each image: a .tiff file and a .tiff original file. You may safely delete the .tiff original files).


## Acknowledgements

This project uses the following external tools and libraries:

- **ThermImageJ** – Glenn J. Tattersall (2019).  
  *Thermal Image Functions and Macros for ImageJ.*  
  [https://doi.org/10.5281/zenodo.2652896](https://doi.org/10.5281/zenodo.2652896)

- **ImageJ** – [https://imagej.net/](https://imagej.net/)  
  Developed by the NIH. Distributed under [Public Domain license](https://imagej.net/ij/docs/intro/license.html).

- **ExifTool** – [https://exiftool.org/](https://exiftool.org/)  
  Developed by Phil Harvey. Distributed under [Artistic License](https://dev.perl.org/licenses/artistic.html).

- **DJI Thermal SDK** – [DJI Official SDK Download](https://terra-1-g.djicdn.com/2640963bcd8e45c0a4f0cb9829739d6b/TSDK/v1.7(12.0-WA345T)/dji_thermal_sdk_v1.7_20241205.zip)  
  Developed by DJI. Distributed under their SDK License Agreement.


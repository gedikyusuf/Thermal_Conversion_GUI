# Thermal_Conversion_GUI
Radiometric JPEG to TIFF conversion process

1-Before running the code, please download and set up the required programs as follows:

  ImageJ: Download from https://wsr.imagej.net/distros/win/ij154-win-java8.zip and extract under the selected root folder as ImageJ/ImageJ.exe.

  DJI Thermal SDK: Download from https://terra-1-g.djicdn.com/2640963bcd8e45c0a4f0cb9829739d6b/TSDK/v1.7(12.0-WA345T)/dji_thermal_sdk_v1.7_20241205.zip and extract under the selected root folder as DJI_Thermal_SDK/.

  ExifTool: Download from https://sourceforge.net/projects/exiftool/files/exiftool-13.34_64.zip/download, extract under the selected root folder, and rename exiftool(-k).exe to exiftool.exe.

  After completing these steps, launch ImageJ.exe and then run the program by double-clicking TC.exe.

2-In the window that opens, go to Step 1: click the "Select Thermal Images Folder" button and choose the folder containing your thermal images. Then, click the "Set Env Vars and Continue" button.

3-In the automatically opened Step 2 tab, click the "Generate RAW Files" button. A command-line window will appear, and the program will start generating .RAW files for your images. Please wait until this process is completed.

4-After that, in the automatically opened Step 3 tab, click the "Convert Files from JPG to TIFF" button.

5-In the automatically opened Step 4 tab, click the "Complete the Process" button to start the final processing step. The processing time depends on the number and size of your images (e.g., converting 100 thermal images typically takes about 5 minutes. In the Converted folder, two files will be created for each image: a .tiff file and a .tiff original file. You may safely delete the .tiff original files).
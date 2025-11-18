import argparse
import sys
import os
import subprocess
import shutil
import tempfile
from .utils import log_message, Configuration
from .exceptions import ThermalConverterError, PathInitializationError, MissingDependencyError

def run_conversion_pipeline(root_path: str) -> None:
    """
    Executes the full R-JPEG to TIFF conversion pipeline without a graphical interface.

    Parameters:
        root_path (str): The root folder containing image files and external tool directories.
    """
    config = Configuration()
    
    try:
        # STEP 1: Initialize and Validate Paths
        config.initialize_paths(root_path)
        config.validate_paths()
        log_message("STEP 1: Paths initialized and external components validated for CLI run.")

        # --- STEP 2: RAW File Generation (DJI IRP) ---
        dji_irp_exe = config.dji_irp_path
        # Windows-specific command adapted for reliable shell execution
        cmd_irp = f'cmd /C "cd /d {config.root_folder} && for %i in (*.JPG) do "{dji_irp_exe}" -a measure -s "%i" -o "%~ni.raw" --measurefmt float32"'
        
        log_message("STEP 2: Starting DJI IRP (RAW generation)...")
        result_irp = subprocess.run(cmd_irp, shell=True, check=False, capture_output=True, text=True)
        if result_irp.returncode != 0:
             raise CommandExecutionError(cmd_irp, f"DJI IRP failed. Stderr: {result_irp.stderr.strip()}")
        log_message("STEP 2: RAW files generated successfully.")


        # --- STEP 3: RAW to TIFF Conversion (ImageJ) ---
        src_folder = config.root_folder
        dest_folder = os.path.join(src_folder, 'converted')
        
        os.makedirs(dest_folder, exist_ok=True)
        macro_arg = f"{src_folder}###{dest_folder}"
        temp_macro = os.path.join(tempfile.gettempdir(), "cli_ysf_temp.ijm")
        shutil.copy2(config.macro_file, temp_macro)

        cmd_imagej = [config.imagej_executable, "--headless", "-macro", temp_macro, macro_arg]
        
        log_message("STEP 3: Starting ImageJ Conversion (RAW to TIFF)...")
        result_imagej = subprocess.run(cmd_imagej, capture_output=True, text=True, check=False)
        
        if result_imagej.returncode != 0:
             raise CommandExecutionError("ImageJ Macro", f"ImageJ conversion failed. Stderr: {result_imagej.stderr.strip()}")
        log_message("STEP 3: ImageJ conversion completed successfully.")


        # --- STEP 4: EXIF Tag Copying (ExifTool) ---
        JPG_files = [f for f in os.listdir(src_folder) if f.lower().endswith('.jpg')]
        if not JPG_files:
            log_message('WARNING: No .JPG files found for tag copying. Skipping STEP 4.')
        
        successful_copies = 0
        for JPG_filename in JPG_files:
            base_name = os.path.splitext(JPG_filename)[0]
            JPG_path = os.path.join(src_folder, JPG_filename)
            dest_path = os.path.join(dest_folder, base_name + '.TIF')

            if not os.path.exists(dest_path):
                log_message(f'WARNING: Target TIF not found for {JPG_filename}. Skipping tag copy.')
                continue

            exiftool_cmd = [
                config.exiftool_exe_path,
                '-TagsFromFile', JPG_path,
                '-all:all', 
                '-overwrite_original', 
                dest_path
            ]
            subprocess.run(exiftool_cmd, check=True, capture_output=True, text=True)
            successful_copies += 1

        log_message(f"STEP 4: Tags copied successfully for {successful_copies} files.")
        log_message("--- CLI Conversion Pipeline Completed Successfully. ---")

    except (ThermalConverterError, subprocess.CalledProcessError) as e:
        log_message(f"CRITICAL ERROR in CLI Pipeline: {e}")
        sys.exit(1)


def cli_main():
    """CLI application entry point, parses arguments and initiates the pipeline."""
    parser = argparse.ArgumentParser(description="ThermalConverter CLI: Automate R-JPEG to TIFF conversion.")
    parser.add_argument('--root', required=True, help="Root folder containing JPGs and external tool directories.")
    
    args = parser.parse_args()
    run_conversion_pipeline(args.root)

if __name__ == '__main__':
    cli_main()

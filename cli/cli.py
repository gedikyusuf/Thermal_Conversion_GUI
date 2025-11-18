# cli/cli.py
"""
Command line interface for headless or scripted usage.
Provides functions to run full pipeline without GUI.
"""
import argparse
from utils.config import Config
from utils.logger import get_logger
from core.raw_processor import generate_raw
from core.imagej_runner import run_imagej_macro
from core.tiff_converter import collect_converted_tifs
from core.exif_manager import batch_copy_tags
import os

logger = get_logger(__name__)

def run_pipeline(config: Config):
    config.resolve_paths_from_root()
    ok = generate_raw(os.path.join(config.dji_folder, 'dji_irp.exe'), config.root_folder)
    if not ok:
        logger.error("RAW generation failed or unsupported.")
    # run imagej macro
    macro_arg = f"{config.root_folder}###{config.output_folder}"
    run_imagej_macro(config.imagej_executable, config.macro_file, macro_arg)
    collect_converted_tifs(config.root_folder, config.output_folder)
    batch_copy_tags(config.exiftool_path, config.root_folder, config.output_folder)
    logger.info("Pipeline finished.")

def parse_args():
    parser = argparse.ArgumentParser(description="Thermal Conversion CLI")
    parser.add_argument("--root", required=True, help="Root folder with JPGs and tool folders")
    parser.add_argument("--imagej", help="Path to ImageJ executable (optional)")
    parser.add_argument("--exiftool", default="exiftool", help="ExifTool command or path")
    return parser.parse_args()

def main():
    args = parse_args()
    cfg = Config(root_folder=args.root, imagej_executable=args.imagej, exiftool_path=args.exiftool)
    run_pipeline(cfg)

if __name__ == "__main__":
    main()

# setup.py
import setuptools
# thermal_converter/__init__.py dosyasında versiyon bilgisi olduğundan, 
# buraya dinamik olarak çekmek için küçük bir hile yapıyoruz.
def get_version():
    with open('thermal_converter/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"\'')
    raise RuntimeError("Unable to find version string.")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thermal-rjpg-converter-gui",
    version=get_version(),
    author="Yusuf Gedik",
    description="A GUI application to convert DJI radiometric RJPG files to TIFFs using DJI SDK, ImageJ, and ExifTool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gedikyusuf/Thermal_Conversion_GUI", 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires='>=3.8',
    install_requires=[
        'PyQt5>=5.15', 
    ],
    # Bu kısım, komut satırından 'thermalconverter' olarak başlatılmasını sağlar
    entry_points={
        'gui_scripts': [
            'thermalconverter = thermal_converter.__main__:main',
        ],
    },
    include_package_data=True,
)

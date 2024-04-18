import sys
from cx_Freeze import setup, Executable

# Name of your main script
main_script = "do.py"

# Dependencies
build_exe_options = {
    "includes": ["PyQt5", "PyPDF2", "keyring", "xhtml2pdf", "reportlab.graphics.barcode.code128","reportlab.platypus.frames"],  # Add missing dependency here
}

# Setup configuration
setup(
    name='Bfinder',
    version='1.0',
    description='Bug and vulnerabilities scanner application',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://Bfinder.com',
    author='therealkelvinmwaijega',
    author_email='mwaijegakelvin9@gmail.com',
    options={"build_exe": build_exe_options},
    executables=[Executable(main_script)],
)

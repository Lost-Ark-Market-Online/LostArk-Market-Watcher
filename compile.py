import PyInstaller.__main__

from modules.config import Config

import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile_from_input_file(
    output_file="file_version_info.txt",
    input_file="metadata.yml",
    version=Config().version
)

PyInstaller.__main__.run([
    'compile.spec',
])
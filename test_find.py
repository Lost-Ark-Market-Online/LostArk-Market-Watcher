import string
import os
import re
from ctypes import windll


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}:\\")
        bitmask >>= 1
    return drives


print(get_drives())


def find_file(root_folder, rex):
    for root, _, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                return os.path.join(root, f)


def find_file_in_all_drives(file_name):
    rex = re.compile(file_name)
    for drive in get_drives():
        return find_file(drive, rex)


lostark_file = find_file_in_all_drives('LOSTARK\.exe')
lostark_directoy = os.path.abspath(os.path.join(
    os.path.dirname(lostark_file), '..', '..'))
print(lostark_directoy)

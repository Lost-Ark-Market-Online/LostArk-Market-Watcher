import easygui
from modules.config import checkconfig

from modules.scan import scan

screenshootsdir, region = checkconfig()
file = easygui.fileopenbox(
    msg="Select the screenshoots directory - (Steam/steamapps/common/Lost Ark/EFGame/Screenshots)",
        title="Innitial configuration", default=screenshootsdir)

res = scan(file, True)
print(res)
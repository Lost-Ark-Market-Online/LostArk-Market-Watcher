import easygui
import os
import configparser

regions = [
    "West North America",
    "East North America",
    "Central Europe",
    "South America",
]


def change_region(old_reg):
    config = configparser.ConfigParser()
    config.read("config.ini")
    c_region = easygui.choicebox(msg='Select a region', title='Region configuration',
                                 choices=regions, preselect=regions.index(old_reg), callback=None, run=True)
    config.set("Config", "region", c_region)
    with open("config.ini", "w") as configfile:
        config.write(configfile)
    return c_region


def change_screenshot_dir(screenshootsdir):
    config = configparser.ConfigParser()
    config.read("config.ini")
    c_screenshootsdir = easygui.diropenbox(
        msg="Select the screenshoots directory - (Steam/steamapps/common/Lost Ark/EFGame/Screenshots)",
        title="Innitial configuration",
        default=screenshootsdir
    )
    config.set("Config", "screenshootsdir", c_screenshootsdir)
    with open("config.ini", "w") as configfile:
        config.write(configfile)
    return c_screenshootsdir


def checkconfig():
    config = configparser.ConfigParser()
    config.read("config.ini")
    screenshootsdir = None
    region = None

    def set_screenshot_dir_config():
        c_screenshootsdir = easygui.diropenbox(
            msg="Select the screenshoots directory - (Steam/steamapps/common/Lost Ark/EFGame/Screenshots)",
            title="Innitial configuration",
        )
        config.set("Config", "screenshootsdir", c_screenshootsdir)
        with open("config.ini", "w") as configfile:
            config.write(configfile)
        return c_screenshootsdir

    def set_region_config():
        c_region = easygui.choicebox(msg='Select a region', title='Region configuration',
                                     choices=regions, preselect=0, callback=None, run=True)
        config.set("Config", "region", c_region)
        with open("config.ini", "w") as configfile:
            config.write(configfile)
        return c_region

    if config.has_section("Config") == False:
        config.add_section("Config")
        
    if(config.has_option("Config", "screenshootsdir") == False):
        screenshootsdir = set_screenshot_dir_config()
    else:
        screenshootsdir = config.get("Config", "screenshootsdir")
        if os.path.exists(screenshootsdir) == False:
            screenshootsdir = set_screenshot_dir_config()

    if(config.has_option("Config", "region") == False):
        region = set_region_config()
    else:
        region = config.get("Config", "region")
        if(region in regions == False):
            region = set_region_config()

    return screenshootsdir, region

import configparser
from modules.errors import NoTokenError, NotConfigured


def get_tokens():
    config = configparser.ConfigParser()
    config.read("config.ini")
    if config.has_section("Token") == False:
        raise NoTokenError()
    else:
        return config.get("Token", "id_token"), config.get("Token", "refresh_token"), config.get("Token", "uid")


def update_token(token):
    config = configparser.ConfigParser()
    config.read("config.ini")

    if config.has_section("Token") == False:
        config.add_section("Token")
        config.set("Token", "refresh_token", token["refresh_token"])
        config.set("Token", "id_token", token["id_token"])
        config.set("Token", "uid", token["uid"])
    else:
        if 'refresh_token' in token:
            config.set("Token", "refresh_token", token["refresh_token"])
        if 'id_token' in token:
            config.set("Token", "id_token", token["id_token"])
        if 'uid' in token:
            config.set("Token", "uid", token["uid"])

    with open("config.ini", "w") as configfile:
        config.write(configfile)


def get_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    if config.has_section("Watcher") == False:
        raise NotConfigured()
    else:
        return config.get("Watcher", "play_audio") == 'True', config.get("Watcher", "delete_screenshots") == 'True', config.get("Watcher", "screenshots_directory")


def update_config(new_config):
    config = configparser.ConfigParser()
    config.read("config.ini")

    if config.has_section("Watcher") == False:
        config.add_section("Watcher")
        config.set("Watcher", "play_audio", new_config["play_audio"])
        config.set("Watcher", "delete_screenshots",
                   new_config["delete_screenshots"])
        config.set("Watcher", "screenshots_directory",
                   new_config["screenshots_directory"])
    else:
        if 'play_audio' in new_config:
            config.set("Watcher", "play_audio", new_config["play_audio"])
        if 'delete_screenshots' in new_config:
            config.set("Watcher", "delete_screenshots",
                       new_config["delete_screenshots"])
        if 'screenshots_directory' in new_config:
            config.set("Watcher", "screenshots_directory",
                       new_config["screenshots_directory"])

    with open("config.ini", "w") as configfile:
        config.write(configfile)

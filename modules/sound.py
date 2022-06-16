import os
import sys
import threading
from time import sleep
import simpleaudio as sa
from threading import Thread
from pycaw.pycaw import AudioUtilities

from PySide6.QtCore import QObject

from modules.common.singleton import Singleton
from modules.config import Config
from modules.logging import AppLogger


class PlaySoundThread(Thread):
    def __init__(self, sound_file):
        Thread.__init__(self)
        self.sound_file = sound_file

    def run(self):
        self.playsound(self.sound_file)

    def playsound(self, file):
        if VolumeController().audio == None:
            VolumeController().searchProcess()
        wave_obj = sa.WaveObject.from_wave_file(file)
        play_obj = wave_obj.play()
        play_obj.wait_done()


def playSuccess():
    PlaySoundThread(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "../assets/sounds/mixkit-achievement-bell-600.wav"))).start()


def playCheck():
    PlaySoundThread(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "../assets/sounds/mixkit-video-game-treasure-2066.wav"))).start()


def playPulse():
    PlaySoundThread(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "../assets/sounds/mixkit-page-forward-single-chime-1107.wav"))).start()


def playError():
    PlaySoundThread(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "../assets/sounds/mixkit-alert-bells-echo-765.wav"))).start()

class VolumeController(metaclass=Singleton):
    sessions = None
    audio = None
    volume = 1.0
    lock = threading.Lock()

    def __init__(self):
        self.sessions = AudioUtilities.GetAllSessions()
        spt = Thread(target=self.searchProcess)
        spt.start()
        
    def searchProcess(self, retries = 0):
        if self.lock.locked() or self.audio:
            return
        file_name = os.path.basename(sys.argv[0])
        self.lock.acquire()
        try:            
            self.sessions = AudioUtilities.GetAllSessions()
            AppLogger().info(f"VolumeController - FileName: {file_name} - retry: {retries}")            
            for session in self.sessions:
                if session.Process and session.Process.name() == file_name:
                    AppLogger().info(f"VolumeController - FileName: {file_name} - Found")
                    self.audio = session.SimpleAudioVolume
                    self.volume = self.audio.GetMasterVolume()
                    self.setVolume(Config().volume/100)
                    break
        except Exception as ex:
            AppLogger().exception(ex)
        
        if(self.audio is None):            
            if retries < 3:
                sleep(2)
                if self.lock.locked():
                    self.lock.release()
                self.searchProcess(retries+1)
            else:
                AppLogger().error(f"VolumeController - FileName: {file_name} - Not Found")
        if self.lock.locked():
            self.lock.release()

    def setVolume(self, volume):
        if self.audio:
            self.audio.SetMasterVolume(volume, None)
        else:
            self.sessions = AudioUtilities.GetAllSessions()
            spt = Thread(target=self.searchProcess)
            spt.start()

import os
import sys
import simpleaudio as sa
from threading import Thread
from pycaw.pycaw import AudioUtilities

from modules.common.singleton import Singleton
from modules.config import Config


class PlaySoundThread(Thread):
    def __init__(self, sound_file):
        Thread.__init__(self)
        self.sound_file = sound_file

    def run(self):
        self.playsound(self.sound_file)

    def playsound(self, file):
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
    audio = None
    volume = 1.0

    def __init__(self):
        sessions = AudioUtilities.GetAllSessions()
        file_name = os.path.basename(sys.executable)

        for session in sessions:
            sav = session.SimpleAudioVolume
            if session.Process and session.Process.name() == file_name:
                self.audio = sav
                self.volume = self.audio.GetMasterVolume()
                self.setVolume(Config().volume/100)
                break
        if self.audio == None:
            raise Exception('Could not find process')

    def setVolume(self, volume):
        if self.audio:
            self.audio.SetMasterVolume(volume, None)

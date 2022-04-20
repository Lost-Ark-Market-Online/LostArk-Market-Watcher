import simpleaudio as sa
import os


def playsound(file):
    wave_obj = sa.WaveObject.from_wave_file(file)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def playSuccess():
    playsound(os.path.abspath(os.path.join(os.path.dirname(__file__),
              "../assets/sounds/mixkit-achievement-bell-600.wav")))


def playCheck():
    playsound(os.path.abspath(os.path.join(os.path.dirname(__file__),
              "../assets/sounds/mixkit-video-game-treasure-2066.wav")))


def playPulse():
    playsound(os.path.abspath(os.path.join(os.path.dirname(__file__),
              "../assets/sounds/mixkit-page-forward-single-chime-1107.wav")))


def playError():
    playsound(os.path.abspath(os.path.join(os.path.dirname(__file__),
              "../assets/sounds/mixkit-alert-bells-echo-765.wav")))

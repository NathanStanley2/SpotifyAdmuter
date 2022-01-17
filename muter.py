#credit to https://github.com/AndreMiras/pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#DO NOT LAUNCH THIS FILE TO START


def volume_muter():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "chrome.exe":
            x = session.SimpleAudioVolume
            x.SetMute(True, None)

def volume_unmuter():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "chrome.exe":
            x = session.SimpleAudioVolume
            x.SetMute(False, None)
    #else:
       # print("not muted")

#mutes the computer with the library


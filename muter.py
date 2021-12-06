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
    #if x == ("a"):
    volume.SetMasterVolumeLevel(-65.25, None) # range is -65.25 to 0, -65 is lowest, 0 is max volume

def volume_unmuter():
    volume.SetMasterVolumeLevel(-5, None) #unmute and set volume to 72
    #else:
       # print("not muted")

#mutes the computer with the library


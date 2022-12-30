from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import pyttsx3

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
audio = pyttsx3.init()
#volume.SetMasterVolumeLevel(-20.0, None)
#volume.SetMute(0,None)

sessions = AudioUtilities.GetAllSessions()
audio.say('Voice 1')
audio.runAndWait()
for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == "chrome.exe":
        audio.say('Voice 2')
        audio.runAndWait()
        volume.SetMasterVolume(0.2, None)
        audio.say('Voice 3')
        audio.runAndWait()
    #if session.Process:
        #print(session.Process.name())

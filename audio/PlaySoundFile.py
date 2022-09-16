from playsound import playsound
import multiprocessing
import pyaudio

audio = ["C:\\Users\\Dante\\Desktop\\Server\\audio\\1_ADDUARSI.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\2_INSEMPRARSI.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\3_INMIARSI_INTUARSI.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\4_SITIRE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\5_INDRACARSI.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\6_ADDENTARE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\7_MUSO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\8_CIGOLARE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\9_MENSOLA.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\10_FERTILE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\11_MUFFA.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\12_ALTO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\13_BELLO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\14_BOCCA.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\15_CASA.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\16_RINGHIARE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\17_SBADIGLIARE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\18_SPUTARE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\19_TESCHIO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\20_UNO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\21_MILLE.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\22_INMILLARSI.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\23_PUNTO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\24_CERCHIO.wav",
         "C:\\Users\\Dante\\Desktop\\Server\\audio\\25_STELLE.wav"]

def Play(i):
    playsound(audio[int(i)])
    
